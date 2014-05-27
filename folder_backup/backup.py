#-*-uncoding=utf-8-*-
import os
import sys
import shutil
import datetime

material_folder=os.path.abspath(r'\\192.168.30.4\Inventory Control Department\1. MATERIAL SYSTEM-1.0')
material_backup_folder=os.path.abspath(r'D:\Material System-1.0')

manpower_folder=os.path.abspath(r'W:\Daily Manpower Record (Monitoring)')
manpower_backup_folder=os.path.abspath(r'D:\Material System-1.0')

def backupMaterial():
	global material_folder,material_backup_folder
	print '1. Now backup Material System'

	a='Material System-1.0 - ' + datetime.datetime.now().strftime('%Y%m%d')
	new_name=os.path.join(material_backup_folder,a)
	if os.path.exists(new_name):
		shutil.rmtree(new_name)
	shutil.copytree(material_folder,new_name)
	print '================copy success!================'
	
	if os.path.exists(new_name):
		print '=====Material System Backup Success!====='
		return True
	else:
		print "#####It's failure.#####"
		return False
		
def backupManpower():
	global manpower_folder,manpower_backup_folder
	print '2. Now backup Manpower System'
	a='MANPOWER RECORD - ' + datetime.datetime.now().strftime('%Y%m%d')
	new_name=os.path.join(manpower_backup_folder,a)
	print new_name
	if os.path.exists(new_name):
		shutil.rmtree(new_name)
		
	shutil.copytree(manpower_folder,new_name)

	if os.path.exists(new_name):
		print '=====MANPOWER RECORD System Backup Success!====='
		return True
	else:
		print "#####It's failure.#####"
		return False

backupMaterial()
backupManpower()

if __name__=='__main__':
	backupManpower()
