#coding:utf-8
#this one is delete repeat date file in Project Code Folder
#the project code file format is like ProjectNameList-CODEBY SHR-2015-01-29-11-01.xlsx.
#and it will move the same day early file to Obseleted folder.

import os
import sys
import shutil

def delfile():

	dir_name,file_name=os.path.split(os.path.abspath(sys.argv[0]))
	new_file=os.path.join(dir_name,"Obseleted")
	if not os.path.isdir(new_file):
		os.mkdir(new_file)
	d={}
	for item in os.listdir(dir_name):
		filename=os.path.join(dir_name,item)
		if item[0]=="~":
			os.remove(filename)
#		print filename
		if os.path.isfile(filename) and (os.path.splitext(filename))[1]==".xlsx":
			name=os.path.basename(filename)
			x=name.split('.')
			i=(x[0]).split('-')
#			print i
			date=''.join(i[2:5])
			time=''.join(i[5:])
#			print "date:  ",date
#			print "time:  ",time
			if d:
				a=d.keys()
				if date in a:
					if int(d[date])<int(time):
						d[str(date)]=str(time)

				else:
					d[str(date)]=str(time)
			else:
				d[str(date)]=str(time)
	m=[]
#	print d
	for k,v in d.iteritems():
#		print k,v
		kv_value="%s-%s-%s-%s-%s"%(str(k[0:4]),str(k[4:6]),str(k[6:]),str(v[:2]),str(v[2:4]))
		m.append(kv_value)
#	print m
	for item in os.listdir(dir_name):
		file_name=os.path.join(dir_name,item)
		new_file_name=os.path.join(new_file,item)
#		print file_name
		name=os.path.basename(file_name)
		x=name.split('.')
		i=(x[0]).split('-')
		da='-'.join(i[2:])
#		print da
		if (os.path.splitext(file_name))[1]==".xlsx" and not da in m:
#			os.remove(file_name)
			shutil.move(file_name,new_file_name)
#			print "%s is deleted."%item

def listfile():
	dir_name,file_name=os.path.split(os.path.abspath(sys.argv[0]))
	for item in os.listdir(dir_name):
		filename=os.path.join(dir_name,item)
		print filename
		print os.path.splitext(filename)
		if os.path.splitext(filename)==".xlsx":
			print filename

#listfile()
delfile()
