#-*-coding=utf-8-*-
#使asynchat的异步服务器
import asynchar,asyncore,socket
import os
import mimetypes

try:
	from http.client import response
except ImportError:
	from httplib import response

#该类到asyncore模块，仅的事件
class async_http(asyncore.dispatcher):
	def __init__(self,port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
		self.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.bind(('',port))
		self.listen(5)

	def handle_accept(self):
		client,addr=self.accept()
		return async_http_handler(client)

#处理异步HTTP
class async_http_handler(asynchat.async_chat):
	def __init__(self,conn=None):
		asynchat.async_chat.__init__(self,conn)
		self.data=[]
		self.got_header=False
		self.set_terminator(b'\r\n\r\n')
	#获取传入数据并区
	def collect_incoming_data(self,data):
		if not self.got_header:
			self.data.append(data)
	#到达终止符
	def found_terminator(self):
		self.got_header=True
		header_data=b''.join(self.data)
		#将报头数据（二进便进一步处理
		heaer_text=header_data.decode('lation-1')
		request=header_lines[0].split()
		op=request[0]
		url=request[1][1:]
		self.process_request(op,url)
	#将文本加入到传出流，但首先要编码
	def push_text(self,text):
		self.push(text.encode('lation-1'))
	#处理
	def process_request(self,op,url):
		if op=='GET':
			if not os.path.exists(url):
				self.send_error(404,'File %s not found\r\n')
			else:
				type,encoding=mimetype.guess_type(url)
				size=os.path.getsize(url)
				self.push_text('HTTP/1.0 200 OK\r\n')
				self.push_text('Content-length: %s\r\n' % size)
				self.push_text('Content-type: %s\r\n' % type)
				self.push_text('\r\n')
				self.push_with_producer(file_producer(url))
		else:
			self.send_error(501,'%s method not implemanted' % op)
		self.close_when_done()

	#错误处理
	def send_error(self,code,message):
		self.push_text('HTTP/1.0 %s %s\r\n' % (code,responses[code]))
		self.push_text('Context-type: text/plain\r\n')
		self.push_text('\r\n')
		self.push_text(message)

class file_producer(object):
	def __init__(self,filename,buffer_size=512):
		self.f=open(filename,'rb')
		self.buffer_size=buffer_size
	def more(self):
		data=self.f.read(self.buffer_size)
		if not data:
			self.f.close()
		return data

a=async_http(8080)
asyncore.loop()
