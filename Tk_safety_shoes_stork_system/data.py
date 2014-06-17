#-*-coding=utf-8-*-
import os
import sqlite3
import datetime
import sys
import shutil

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
FILENAME=os.path.join(FILEPATH,'safety.db')

USER=os.path.join(FILEPATH,'user.txt')
STATUS=os.path.join(FILEPATH,'status.txt')
PRODUCTNAME=os.path.join(FILEPATH,'productname.txt')

def main_process(*args):
	m=args
	try:
		db=sqlite3.connect(FILENAME)
		db.text_factory=str
		cursor=db.cursor()
		if len(m)==1:
			cursor.execute(m[0])
		else:
			cursor.execute(m[0],m[1])
		db.commit()
	except Exception as e:
		db.rollback()
		print e
	finally:
		db.close()

def create_table():
	content='''CREATE TABLE safety_shoes(id INTEGER PRIMARY KEY NOT NULL,issue_from TEXT NOT NULL,issue_to TEXT NOT NULL,product_name TEXT NOT NULL,size TEXT NOT NULL,qty TEXT,issue_date TEXT,issue_status TEXT,remarks TEXT,create_by TEXT,create_date TEXT)'''
	main_process(content)
	
def get_data():
	try:
		db=sqlite3.connect(FILENAME)
		c=db.cursor()
		c.execute('SELECT * FROM safety_shoes')
		x=[]
		for i in c.fetchall():
			m={'id':i[0],'issue_from':i[1],'issue_to':i[2],'product_name':i[3],	'size':i[4],'qty':i[5],'issue_date':i[6],'issue_status':i[7],'remarks':i[8],'create_by':i[9],'create_date':i[10]}
			x.append(m)
		db.commit()
		return x
	except Exception as e:
		db.rollback()
		print e
	finally:
		db.close()

def search_report(**kwargs):
	"kwargs is dictionary follow {'id':'','issue_from':'','issue_to':'',...}, in this dictionary only keep true value."
	if kwargs:
		x=set(kwargs.values)
		m=get_data()
		s=[]
		for i in m:
			a=set(i.values)		
			if a.issuperset(x):
				s.append(i)
		return s		
		
def add(inv_list):
	if inv_list:
		content='''INSERT INTO safety_shoes(issue_from,issue_to,product_name,size,qty,issue_date,issue_status,remarks,create_by,create_date) VALUES(?,?,?,?,?,?,?,?,?,?)'''
		values=tuple(inv_list)
		main_process(content,values)
		return True

def update(inv_id,inv_list):
	if inv_id and inv_list:
		content='''UPDATE safety_shoes SET issue_from=?, issue_to=?, product_name=?, size=?, qty=?, issue_date=?, issue_status=?, remarks=?, create_by=?, create_date=? WHERE id=?'''
		m=inv_list.append(inv_id)
		values=tuple(inv_list)
		#values=(','.join(inv_list),int(inv_id))
		main_process(content,values)
		return True
		
def delete(inv_id):
	if inv_id:
		content='''DELETE FROM safety_shoes WHERE id=?'''
		values=(inv_id,)
		main_process(content,values)
		return True

#==========LOGIN IN===========
def get_name():
	a=[]
	with open(USER,'r') as f:
		for i in f.readlines():
			m={}
			x=i.split(',')
			m['username']=x[0]
			m['password']=x[1]
			a.append(m)
	return a

#==========status================
def get_status():
	a=[]
	with open(STATUS,'r') as f:
		for i in f.readlines():
			a.append(i)
	return a		
	
#==========product name===========
def get_product_name():
	a=[]
	with open(PRODUCTNAME,'r') as f:
		for i in f.readlines():
			a.append(i)
	return a


def get_items(filename):
	a=[]
	with open(filename,'r') as f:
		for i in f.readlines():
			if i.strip(''):
				a.append(i)
	return a		

def add_items(filename,items):
	'items is str'
	with open(filename,'a') as f:
		f.waitlines(items) #waitlines wait many lines
		return True

def del_items(filename,items):
	'items is str'
	newfilename=os.path.splitext(filename)[0] + '_new' + os.path.splitext(filename)[-1]
	with open(filename,'r') as f:
		with open(newfilename,'w') as g:
			if i in f.readlines():
				if i != upper(items):
					g.write(i)
	shutil.move()	

#==========employee name list===========
def get_name_list():
	m=r'\\KMSVR\Company Data\Common\2. KM Software\backup'
	project_file=os.path.join(m,'namebackup.txt')
	pl=os.path.join(os.path.split(sys.argv[0])[0],'data')
	project_list=os.path.join(pl,'namebackup.txt')
	print os.path.split(sys.argv[0])[0]
	try:
		shutil.copy(project_file,project_list)
	except Exception as e:
		print e
	#print project_list
	x=[]
	with open(project_list,'r') as f:
		for i in f.readlines():
			if i:
				n=i.strip('')
				x.append(n.split(','))
	#print x
	return x
	
def insertTest():
	content='''INSERT INTO safety_shoes(issue_from,issue_to,product_name,size,qty,issue_date,issue_status,remarks,create_by,create_date) VALUES(?,?,?,?,?,?,?,?,?,?)'''
	values=('1','2','3','4','5','6','7','8','9','10')
	main_process(content,values)
	return True

if __name__=='__main__':
	create_table()
	insertTest()
	for i in get_data():
		print i
