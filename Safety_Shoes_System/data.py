#-*-coding=utf-8-*-
import os
import sqlite3
import datetime
import sys
import shutil


FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
FILENAME=os.path.join(FILEPATH,'system.db')

USER=os.path.join(FILEPATH,'user.txt')
STATUS=os.path.join(FILEPATH,'status.txt')
PRODUCTNAME=os.path.join(FILEPATH,'productname.txt')
ISSUE_KINDS=os.path.join(FILEPATH,'issue_kind.txt')


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
		print "finish"
	except Exception as e:
		db.rollback()
		print e
	finally:
		db.close()

def create_table(tablename=None,*args):
	content="DROP TABLE if exists "+tablename
	main_process(content)
	c=(' TEXT, '.join(args[0]))+' TEXT'
	content='''CREATE TABLE %s(id INTEGER PRIMARY KEY NOT NULL,%s)'''%(tablename,c)
#	print content
		#issue_from TEXT NOT NULL,issue_to TEXT NOT NULL,product_name TEXT NOT NULL,size TEXT NOT NULL,qty TEXT,issue_date TEXT,issue_status TEXT,issue_kind TEXT,remarks TEXT,create_by TEXT,create_date TEXT)'''%(tablename,)
	main_process(content)
	
def get_data(tablename=None,*args):
	try:
		db=sqlite3.connect(FILENAME)
		c=db.cursor()
		c.execute('SELECT * FROM %s'%(tablename,))
		x=[]
		tableitem=args[0]
		if tableitem[0]!="id":
			tableitem.insert(0,'id')
		for i in c.fetchall():
			m=dict(zip(tableitem,i))
#			m={'id':i[0],'issue_from':i[1],'issue_to':i[2],'product_name':i[3],	'size':i[4],'qty':i[5],'issue_date':i[6],'issue_status':i[7],'issue_kind':i[8],'remarks':i[9],'create_by':i[10],'create_date':i[11]}
			x.append(m)
		db.commit()
#		print x
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
		
def add(tablename=None,inv_list=None):
	if inv_list:
		if tablename=='safety_shoes':
			content='''INSERT INTO safety_shoes(issue_status,issue_from,issue_to,issue_date,issue_type,issue_size,issue_qty,issue_product,remarks,create_by,create_date) VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
			values=tuple(inv_list)
			main_process(content,values)
			return True
		elif tablename=='tshirt':
			content='''INSERT INTO tshirt(issue_status,issue_from,issue_to,issue_date,issue_type,issue_size,issue_qty,issue_color,issue_sex,issue_sleeve,issue_pocket,remarks,create_by,create_date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
			values=tuple(inv_list)
			main_process(content,values)
			return True

def update(tablename=None,inv_id=None,*inv_list):
	if inv_id and inv_list:
		if tablename=='safety_shoes':
			content='''UPDATE safety_shoes SET issue_status=?,issue_from=?,issue_to=?,issue_date=?,issue_type=?,issue_size=?,issue_qty=?,issue_product=?,remarks=?,create_by=?,create_date=? WHERE id=?'''
			m=inv_list[0].append(inv_id)
			values=tuple(inv_list)
			#values=(','.join(inv_list),int(inv_id))
			main_process(content,values[0])
			return True
		elif tablename=='tshirt':
			content='''UPDATE tshirt SET issue_status=?,issue_from=?,issue_to=?,issue_date=?,issue_type=?,issue_size=?,issue_qty=?,issue_color=?,issue_sex=?,issue_sleeve=?,issue_pocket=?,remarks=?,create_by=?,create_date=? WHERE id=?'''
			m=inv_list.append(inv_id)
			values=tuple(inv_list)
			#values=(','.join(inv_list),int(inv_id))
			main_process(content,values)
			return True
		
def delete(tablename,inv_id):
	if inv_id:
		if tablename=='safety_shoes':
			content='''DELETE FROM safety_shoes WHERE id=? '''
		elif tablename=='tshirt':
			content='''DELETE FROM tshirt WHERE id=? '''
		print content
		values=(inv_id,)
		print values
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
			x=i.strip('\n')
			if x:
				a.append(x)
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


#===========issue kinds============
def get_issue_list():
	a=[]
	with open(ISSUE_KINDS,'r') as f:
		for i in f.readlines():
			a.append(i.strip('').strip('\n'))
	return a

#==========employee name list===========
def get_name_list():
	m=r'\\192.168.20.15\Company Data\Common\2. KM Software\backup'
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
	content='''INSERT INTO safety_shoes(issue_from,issue_to,product_name,size,qty,issue_date,issue_status,issue_kind,remarks,create_by,create_date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
	values=('1','2','3','4','5','6','7','8','9','10','11')
	main_process(content,values)
	return True

if __name__=='__main__':
#	c=['issue_status','issue_from','issue_to','issue_date','issue_type','issue_size','issue_qty','issue_product','remarks','create_by','create_date']
##	create_table('safety_shoes',c)
##	m=['issue_status','issue_from','issue_to','issue_date','issue_type','issue_size','issue_qty','issue_color','issue_sex','issue_sleeve','issue_pocket','remarks','create_by','create_date']
##	create_table('tshirt',m)
##	get_data('safety_shoes',c)
#					'Status',			'From Location',	'To Location',			'Date',		'Type','Size','Qty','Color','Sex','Sleeve','Pocket','Remark','Create By','Create Date'
	for i in range(20):
		inv_list=('OFFICE to STORE','OS00218 TONY TAN YONG','OS00218 TONY TAN YONG','2015/03/19','ISSUE','L',int(i+1),'WHITE','MALE','LONG','YES','REMARK '+str(i),'Tony Tan','2015/03/19')
		print str(i)
		add('tshirt',inv_list)
#	delete('safety_shoes','5')
