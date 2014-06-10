#-*-coding=utf-8-*-
import os
try:
	from httplib import HTTPConnection
except ImportError:
	from http.client import HTTPConnection

BOUNDARY="$Python-Essental-Reference$"
CRLF="\R\N"

def upload(addr,url,formfields,filefields):
	#为表单字段创建区
	formsections=[]
	for name in formfields:
		section=[
			'--'+BOUNDARY,
			'Content-disposition: form-data; name="%s"' % name,
			'',
			formfields[name]
			]
		formsections.append(CRLF.join(sction)+CRLF)

	#收集要所有文件信息
	fileinfo=[(os.path.getsize(filename),formname,filename) for formname,filename in filefields.items()]
	#为每个文件创建HTTP报头
	filebytes=0
	fileheaders=[]
	for filesize,formname,filename in fileinfo:
		headers=[
			'--' + BOUNDARY,
			'Content-Disposition: form-data; name="%s"; filename="%s"' % (formname,filename),
			'Content-length: %d' % filesize,
			''
			]
		fileheaders.append(CRLF.join(headers) + CRLF)
		filebytes += filesize

	#关闭marker
	closing='--' + BOUNDARY + '--\r\n'
	#确整个请求的长度
	content_size=(sum(len(f) for f in formsections) + sum(len(f) for f in fileheaders) + filebytes + len(closing))
	#上传
	conn=HTTPConnection(*addr)
	conn.putrequest('POST',url)
	conn.putheader('Content-type','multipart/form-data; boundary=%s' % BOUNDARY)
	conn.putheadder('Content-length',str(content_size))
	conn.endheaders()
	#发送所有表单区
	for s in formsections:
		conn.send(s.encode('utf-8'))
	#发送所有文件
	for head,filename in zip(fileheaders,filefields.values()):
		conn.send(head.encode('utf-8'))
		f=open(filename,'rb')
		while True:
			chunk=f.read(16384)
			if not chunk: break
			conn.send(chunk)
		f.close()
	conn.send(closing.encode('utf-8'))
	r=conn.getrespnse()
	responsedata=r.read()
	conn.close()
	return responsedata

#示例：上传一些‘name','email'
#file_1,file_2是远程服务器
server=('localhost',8080)
url='/cgi-bin/upload.py'
formfields={'name':'Dave','email':'dave@dabeaz.com'}
filefields={'file_1':'IMG_1008.JPG','file_2':'IMG_1757.JPG'}
resp=upload(server,url,formfields,filefields)
print resp
