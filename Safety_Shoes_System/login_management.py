#coding:utf-8
import os,sys
import tempfile

class LoginManagement:
	def __init__(self):
		self.createFolder()	
		self.loginfilename='loginmag.txt'
	def createFolder(self):
		os.chdir('c:\\')
		if os.path.exists('c:\\temp') is False:
			os.mkdir('c:\\temp')
#		print os.path.exists('c:\\temp')
		self.folderpath=os.path.join('c:\\temp','loginmag')
		if not os.path.exists(self.folderpath):
			os.mkdir(self.folderpath)
			print os.path.exists(self.folderpath)
	def createFile(self,username=None):
#		print "Current Path:   ",os.getcwd()
#		print 'folderpath: ',self.folderpath
		try:
			os.remove(os.path.join(self.folderpath,self.loginfilename))
		except:
			pass
		filename=os.path.join(self.folderpath,self.loginfilename)
#		print filename
#		print os.path.exists(self.folderpath)
		with open(filename,'w') as f:
			f.write(username.upper())
			return True
	def removeFile(self):
		filename=os.path.join(self.folderpath,self.loginfilename)
		if os.path.exists(filename):
			try:
				os.remove(filename)
				return True
			except:
				return False
		else:
			return True
	def readName(self):
		filename=os.path.join(self.folderpath,self.loginfilename)
		try:
			with open(filename,'r') as f:
				n=f.readlines()
				if n:
					return str(n[0])
				return False
		except:
			return False
	def Logged(self):
		filename=os.path.join(self.folderpath,self.loginfilename)
		try:
			with(filename,'r') as f:
				if f.readlines():
					return True
				else:
					return False
		except:
			return False
	def isAdmin(self):
		filename=os.path.join(self.folderpath,self.loginfilename)
		try:
			with(filename,'r') as f:
				n=f.readlines()
				if n=='ADMIN':
					return True
				return False
		except:
			return False
		
if __name__=='__main__':
	l=LoginManagement()
	l.createFile(username='Tony tan')
