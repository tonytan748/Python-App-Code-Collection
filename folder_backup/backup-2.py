#-*-coding=utf-8-*-
import os
import shutil
import datetime
# 设置待备份的源文件夹及存放备份文件的目标文件夹
material_backup_folder = os.path.abspath(r'D:\Material System-1.0')

srcDir = os.path.abspath(r'\\192.168.30.4\Inventory Control Department\1. MATERIAL SYSTEM-1.0')
a='Material System-1.0 - ' + datetime.datetime.now().strftime('%Y%m%d')
dstDir=os.path.join(material_backup_folder,a)

mansrcDir=os.path.abspath(r'W:\Daily Manpower Record (Monitoring)')
b='MANPOWER RECORD - ' + datetime.datetime.now().strftime('%Y%m%d')
manDir=os.path.join(material_backup_folder,b)

# 目录递归拷贝函数
def dir_copyTree(src, dst):
	names = os.listdir(src)
	# 目标文件夹不存在，则新建
	if not os.path.exists(dst):
		os.mkdir(dst)
	# 遍历源文件夹中的文件与文件夹
	for name in names:
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			# 是文件夹则递归调用本拷贝函数，否则直接拷贝文件
			if os.path.isdir(srcname):                
				dir_copyTree(srcname, dstname)
			else:
				if (not os.path.exists(dstname) or ((os.path.exists(dstname)) and (os.path.getsize(dstname) != os.path.getsize(srcname)))):
					print dstname
					shutil.copy2(srcname, dst)
		except:
			error.traceback();
			raise
# 备份函数
def dir_backup():
	global srcDir
	global dstDir
	global mansrcDir
	global manDir
	print "Source Folder" + srcDir
	print "Destination Folder" + dstDir
	print "The copy  of the Document:"
	dir_copyTree(srcDir, dstDir)
	# 将此句注释则会一闪而过，方便自动备份
	print "=========================================================="
	print "========================================================"
	print "======================================================"
	print "===================================================="
	print "=================================================="
	print "================================================"
	print "=============================================="
	print "============================================"
	print "=========================================="
	print "========================================"
	print "======================================"
	print "===================================="
	print "=================================="
	print "================================"
	print "============================"
	print "=========================="
	print "========================"
	print "======================"
	print "===================="
	print "=================="
	print "================"
	print "=============="
	print "============"
	dir_copyTree(mansrcDir, manDir)
	raw_input ("The backup is complete.")
# 执行备份函数
dir_backup()