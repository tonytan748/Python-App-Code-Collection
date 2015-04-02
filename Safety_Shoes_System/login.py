
import os,sys
from Tkinter import *
import tkMessageBox
import ttk
import datetime
import data

from config import *
from login_management import LoginManagement
GET_USER

import pim

class Login(object):
	def __init__(self,master,info='Login'):
		self.ma=master

		Label(self.ma,text="User Name:").grid(row=0,column=0,sticky=W)
		Label(self.ma,text='Password:').grid(row=1,column=0,sticky=W)

		self.userlist=[(i.split(','))[0] for i in GET_USER]
		self.userEntry=ttk.Combobox(self.ma)
		self.userEntry['values']=tuple(self.userlist)
		self.userEntry['width']=20
		self.userEntry.grid(row=0,column=1,columnspan=2,sticky=W,pady=5)

		self.pwdEntry=Entry(self.ma,show='*')
		self.pwdEntry.bind('<Return>',self.loginit)
		self.pwdEntry.grid(row=1,column=1,columnspan=2,sticky=W,pady=5)

		self.submit=Button(self.ma,text="LOGIN",command=self.login,padx=3,pady=5)
		self.submit.grid(row=2,column=1,sticky=W)

		self.clean=Button(self.ma,text='CLEAN',command=self.clear,pady=5)
		self.clean.grid(row=2,column=2,sticky=W)

	def loginit(self,event):
		self.login()

	def login(self):
		self.username=self.userEntry.get()
		self.password=self.pwdEntry.get()
		print self.username
		print self.password
		if self.username!=None and self.password!=None: 
			isu=False
			for i in GET_USER:
				m=i.split(',')
				if self.username==m[0] and self.password==m[1]:
					isu=True
					break	
			if isu:
				l=LoginManagement()
				x=l.createFile(username=self.username)
				print x
				pim.PIM()
			else:
				tkMessageBox.showinfo('ERROR','Please check your username and password')
				return
		else:
			tkMessageBox.showinfo('ERROR','Please check your username and password')
			return

	def clear(self):
		self.userEntry.delete(0,END)
		self.pwdEntry.delete(0,END)
 

def main():
	root=Tk()
	user_name=Login(root)
	mainloop()
	
if __name__=="__main__":
	main()