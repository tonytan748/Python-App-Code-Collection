#coding:utf-8
from editor import Editor
from editable import Editable
import Tkinter
import ttk
import tkMessageBox
import tkFileDialog
import datetime,time
import os,sys
from Tkinter import *

from config_safetyshoes import *
from config import *
import data

from report import Report
from login_management import LoginManagement


class EditableSafetyShoes(Editable):
	def __init__(self,master):
		self.master=master
		self.editor=SafetyShoesEditor(self)

	def getEditor(self):
		return self.editor

class SafetyShoesEditor(Editor,Tkinter.Frame):
	def __init__(self,owner):
		Tkinter.Frame.__init__(self,owner.master)
		self.owner=owner

		self.DATALIST=None
		x=LoginManagement()
		self.username=x.readName()
		print "username: %s"%(self.username)

		toolbar=Frame(self,bd=1,relief=RAISED)
		Label(toolbar,text="STATUS",font=('Verdana',(8))).grid(row=0,column=0,sticky=W)
		Label(toolbar,text='DATE',font=('Verdana',(8))).grid(row=0,column=2,sticky=W)
		Label(toolbar,text='SIZE',font=('Verdana',(8))).grid(row=0,column=4,sticky=W)
		Label(toolbar,text='QTY',font=('Verdana',(8))).grid(row=0,column=6,sticky=W)
		Label(toolbar,text='REMARK',font=('Verdana',(8))).grid(row=0,column=8,sticky=W)

		Label(toolbar,text='FROM',font=('Verdana',(8))).grid(row=1,column=0,sticky=W)
		Label(toolbar,text='TYPE',font=('Verdana',(8))).grid(row=1,column=2,sticky=W)

		Label(toolbar,text='PRODUCT',font=('Verdana',(8))).grid(row=1,column=4,sticky=W)

		Label(toolbar,text='TO',font=('Verdana',(8))).grid(row=2,column=0,sticky=W)
		Label(toolbar,text='ID',font=('Verdana',(8))).grid(row=2,column=2,sticky=W)

		#=====STATUS======
		statuslist=[i for i in GET_STATUS]
		self.status=ttk.Combobox(toolbar,font=('Verdana',(8)))
		self.status['values']=tuple(statuslist)
		self.status['width']=25
		self.status.grid(row=0,column=1,sticky=W+N,pady=2)
		#========ISSUE FROM========
		fromlocal=[i[1]+'  '+i[0] for i in GET_NAMES if (i[1]!="")]
		self.fromL=ttk.Combobox(toolbar,font=('Verdana',(8)),height=25)
		self.fromL['values']=tuple(fromlocal)
		self.fromL['width']=25
		self.fromL.bind('<Return>',self.getFromName)
		self.fromL.grid(row=1,column=1,sticky=W+N,pady=2)
		#========ISSUE TO========
		self.toL=ttk.Combobox(toolbar,font=('Verdana',(8)),height=25)
		self.toL['values']=tuple(fromlocal)
		self.toL['width']=25
		self.toL.bind('<Return>',self.getToName)
		self.toL.grid(row=2,column=1,sticky=W+N,pady=2)

		self.dateframe=Frame(toolbar)
		#=====DATE======
		self.date=StringVar(self.dateframe)
		self.getdate=Entry(self.dateframe,font=('Verdana',(8)),textvariable=self.date).grid(row=0,column=1,sticky=W+N)
		self.date.set(datetime.datetime.now().strftime('%Y/%m/%d'))
		#========TODAY========
		Button(self.dateframe,text='TODAY',command=self.get_today,width=5,font=('Verdana',(6))).grid(row=0,column=2,sticky=W+N)
		self.dateframe.grid(row=0,column=3,sticky=W+N,pady=2)

		#========TYPE===========
		type_list=[i for i in GET_TYPE]
		self.type=ttk.Combobox(toolbar,font=('Verdana',(8)))
		self.type['values']=tuple(type_list)
		self.type['width']=15
		self.type.set(type_list[0])
		self.type.grid(row=1,column=3,sticky=W,pady=2)
		#=========ID==========
		self.id=StringVar(self.dateframe)
		Label(toolbar,font=('Verdana',(8)),textvariable=self.id).grid(row=2,column=3,sticky=W,pady=2)
		self.id.set('')

		#========SIZE==========
		sizelist=range(4,14)
		self.size=ttk.Combobox(toolbar,font=('Verdana',(8)))
		self.size['values']=tuple(sizelist)
		self.size['width']=10
		self.size.set(sizelist[2])
		self.size.grid(row=0,column=5,sticky=W,pady=2)
		#=========QTY=========
		self.qty=StringVar(self.dateframe)
		self.getqty=Entry(toolbar,font=('Verdana',(8)),textvariable=self.qty,width=13)
		self.getqty.grid(row=0,column=7,sticky=W,pady=2)

		#========PRODUCT==========
		productlist=[i for i in GET_PRODUCT]
		self.product=ttk.Combobox(toolbar,font=('Verdana',(8)))
		self.product['values']=tuple(productlist)
		self.product['width']=30
		self.product.set(productlist[0])
		self.product.grid(row=1,column=5,columnspan=3,sticky=W+N,pady=2)

		#========REMARK===========
		f1=Frame(toolbar)
		bary1=Scrollbar(f1)
		bary1.pack(side=RIGHT,fill=Y)
		self.remark=Text(f1,font=('Verdana',(8)),width=20,height=2)
		self.remark.pack(side=LEFT,fill=BOTH)
		bary1.config(command=self.remark.yview)
		self.remark.config(yscrollcommand=bary1.set)
		f1.grid(row=1,column=8,rowspan=2,sticky=W+N,pady=2,padx=3)

		#=========REPORT BUTTON==========
		reportframe=Frame(toolbar,padx=3)
		Button(reportframe,text='ISSUANCE REPORT',command=self.issuereport,width=15,font=('Verdana',(8))).grid(row=0,column=0,sticky=W+N,pady=2)
		Button(reportframe,text='LOAN REPORT',command=self.lendreport,width=15,font=('Verdana',(8))).grid(row=1,column=0,sticky=W+N,pady=2)
		Button(reportframe,text='STOCK REPORT',command=self.stockreport,width=15,font=('Verdana',(8))).grid(row=2,column=0,sticky=W+N,pady=2)
		reportframe.grid(row=0,column=9,rowspan=3,sticky=W+N)

		#=========buttons==========
		toolbar.pack(side=TOP,fill=X)
		
		btnbar=Frame(self)
		self.addbtn=Button(btnbar,text='ADD',command=self.addItem,width=10,font=('Verdana',(8))).grid(row=0,column=0,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=1)
		self.editbtn=Button(btnbar,text='EDIT',command=self.editItem,width=10,font=('Verdana',(8))).grid(row=0,column=2,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=3)
		self.delbtn=Button(btnbar,text='DELETE',command=self.delItem,width=10,font=('Verdana',(8))).grid(row=0,column=4,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=5)
		self.clear=Button(btnbar,text='CLEAN',command=self.clearItem,width=10,font=('Verdana',(8))).grid(row=0,column=6,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=7)
		self.search=Button(btnbar,text='SEARCH',command=self.searchItem,width=10,font=('Verdana',(8))).grid(row=0,column=8,sticky=W)
		btnbar.pack(side=TOP,fill=X,pady=3)
		
		#=========ISSUE LIST============
		issue_list=['ID','STATUS','FROM','TO','DATE','TYPE','SIZE','QTY','PRODUCT','REMARK','CREATE BY','CREATE_DATE']
		listbar=Frame(self)

		bary2=Scrollbar(listbar)
		bary2.pack(side=RIGHT,fill=Y)
		barx2=Scrollbar(listbar,orient=HORIZONTAL)
		barx2.pack(side=BOTTOM,fill=X)

		self.issuelist=ttk.Treeview(listbar,columns=issue_list)
		self.issuelist.column(column='#0',width=0,stretch=False)
		for i in range(len(issue_list)):
			self.issuelist.heading(i,text=issue_list[i])
			self.issuelist.column(i,width=60)
		self.issuelist.column(0,width=30)
		self.issuelist.column(1,width=130)
		self.issuelist.column(2,width=200)	
		self.issuelist.column(3,width=200)
		self.issuelist['height']=25
		self.issuelist.bind('<<TreeviewSelect>>',self.getIssueItem)
		self.issuelist.pack(side=LEFT,fill=BOTH)

		barx2.config(command=self.issuelist.xview)
		bary2.config(command=self.issuelist.yview)

		self.issuelist.config(xscrollcommand=barx2.set,yscrollcommand=bary2)
		listbar.pack(fill=X)
		
		#========PAGES MANAGEMENT==========
		pagebar=Frame(self)
		self.providerbtn=Button(pagebar,text="PROVIDER",command=self.providerpage).pack(side=LEFT,padx=5)
		self.pages=StringVar(self.dateframe)
		self.page_pages=Label(pagebar,textvariable=self.pages).pack(side=LEFT,padx=5)
		self.pages.set('1/1')
		self.nextbar=Button(pagebar,text='Next',command=self.nextpage).pack(side=LEFT,padx=5)
		pagebar.pack(fill=X)

		#=========SHOW ISSUE LIST ITEMS===========
		self.get_item_list()

	############################
	### SHOW THE REPORT LIST ###
	############################
	def get_item_list(self):
		self.DATALIST=[]
		if self.issuelist.get_children():
			for i in self.issuelist.get_children():
				self.issuelist.delete(i)
		m=data.get_data('safety_shoes',['issue_status','issue_from','issue_to','issue_date','issue_type','issue_size','issue_qty','issue_product','remarks','create_by','create_date'])
		if m:
			self.DATALIST.extend(m)
			if len(m)>25:
				if len(m)%25==0:
					pages=len(m)/25
				else:
					pages=len(m)/25+1
				p='1/' + str(pages)
				self.pages.set(p)
				for i in m[:25]:
					x=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['issue_type'],i['issue_size'],i['issue_qty'],i['issue_product'],i['remarks'],i['create_by'],i['create_date']]
					self.issuelist.insert('','end',values=x)
			else:
				self.pages.set('1/1')
				for i in m:
					x=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['issue_type'],i['issue_size'],i['issue_qty'],i['issue_product'],i['remarks'],i['create_by'],i['create_date']]
					self.issuelist.insert('','end',values=x)
	#############
	### TODAY ###
	#############
	def get_today(self):
		today=datetime.datetime.today().strftime('%Y/%m/%d')
		self.date.set(today)
		print self.date.get()
	#######################################
	### SHORTCUT FOR KEY IN EMPLOYER ID ###
	#######################################
	def getFromName(self,event):
		if self.fromL.get():
			a=[i for i in GET_NAMES if self.fromL.get().upper() in i[1].strip()]
			if a:
				fullname=a[0][1] + '  ' + a[0][0]
				self.fromL.delete(0,END)
				self.fromL.insert(0,fullname)
	def getToName(self,event):
		if self.toL.get():
			a=[i for i in GET_NAMES if self.toL.get().upper() in i[1].strip()]
			if a:
				fullname=a[0][1] + '  ' + a[0][0]
				self.toL.delete(0,END)
				self.toL.insert(0,fullname)

	######################
	### *** REPORT *** ###
	######################
	def issuereport(self):
		name=os.path.join(FILEPATH,'safety_shoes_issue_report.csv')
		temp_issue_worker_report=tkFileDialog.asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,title='Save')

		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		x=Report('safety_shoes')
		x.output_safetyshoes(temp_issue_worker_report,'issue')
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	def lendreport(self):
		name=os.path.join(FILEPATH,'safety_shoes_lend_report.csv')
		temp_issue_worker_report=tkFileDialog.asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,title='Save')

		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		x=Report('safety_shoes')
		x.output_safetyshoes(temp_issue_worker_report,'lend')
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	def stockreport(self):
		name=os.path.join(FILEPATH,'safety_shoes_stock_report.csv')
		temp_issue_worker_report=tkFileDialog.asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,title='Save')
		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		x=Report('safety_shoes')
		x.stock_safetyshoes(temp_issue_worker_report)
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	####################
	### EDIT BUTTONS ###
	####################
	def getIssueItem(self,event):
		self.clearItem()
		self.id.set('')
		m=self.issuelist.selection()
#		print m
		if m:
			x=self.issuelist.item(m)['values']
#			print x
			s_list=dict(id=x[0],issue_status=x[1],issue_from=x[2],issue_to=x[3],issue_date=x[4],issue_type=x[5],issue_size=x[6],issue_qty=x[7],issue_product=x[8],remarks=x[9],create_by=x[10],create_date=x[11])
#			s_list=dict(id=x[0],status=x[1],fromL=x[2],toL=x[3],date=x[4],product=x[5],size=x[6],qty=x[7],issue_kind=x[8],remark=x[9],create_by=x[10],create_date=x[11])
			self.status.set(s_list['issue_status'])
			self.fromL.set(s_list['issue_from'])
			self.toL.set(s_list['issue_to'])
			self.date.set(s_list['issue_date'])
			self.product.insert(0,s_list['issue_product'])
			self.size.set(s_list['issue_size'])
			self.qty.set(s_list['issue_qty'])
			self.id.set(s_list['id'])
			self.type.set(s_list['issue_type'])
			self.remark.insert(0.0,s_list['remarks'])

	def addItem(self):
		print "Add Item"
		if self.id.get():
			tkMessageBox.showinfo('Notice','This is a exust report,\nPlease clean it and try again.')
			return False
		if self.isstatus() is False:
			self.status.focus_set()
			return False
		if self.issize() is False:
			self.size.focus_set()
			return False
		if self.isqty() is False:
			self.getqty.focus_set()
			return False
		if self.istype() is False:
			self.type.focus_set()
			return False
		if self.isfromL() is False:
			self.fromL.focus_set()
			return False
		if self.istoL() is False:
			self.toL.focus_set()
			return False

		issue_status=self.isvalue(self.status.get())
		issue_from=self.isvalue(self.fromL.get())
		issue_to=self.isvalue(self.toL.get())
		issue_date=self.isvalue(self.date.get())
		issue_size=self.isvalue(self.size.get())
		issue_product=self.isvalue(self.product.get())
		issue_qty=self.isvalue(self.qty.get())
		issue_type=self.isvalue(self.type.get())
		remarks=self.isvalue(self.remark.get(1.0,END))
		create_by=self.username
		create_date=datetime.datetime.now().strftime('%Y/%m/%d-%H%M')

		add_list=[issue_status,issue_from,issue_to,issue_date,issue_type,issue_size,issue_qty,issue_product,remarks,create_by,create_date]
		a=data.add('safety_shoes',add_list)
		if a:
			tkMessageBox.showinfo('Notice','Add Success.')
			self.clearItem()
			self.get_item_list()
			self.id.set('')
			self.get_first_page()
			self.status.focus_set()
		else:
			tkMessageBox.showinfo('Notice','please try again.')
			self.status.focus_set()
			return False

	def editItem(self):
		print "Edit Item"
		if self.isstatus() is False:
			self.status.focus_set()
			return False
		if self.issize() is False:
			self.size.focus_set()
			return False
		if self.isqty() is False:
			self.getqty.focus_get()
			return False
		if self.id.get():
			item_id= str(self.id.get())
			m=[str(i['id']) for i in GET_ITEMS]
			if item_id in m:
				eid=self.id.get()
				print eid
				issue_status=self.isvalue(self.status.get())
				issue_from=self.isvalue(self.fromL.get())
				issue_to=self.isvalue(self.toL.get())
				issue_date=self.isvalue(self.date.get())
				issue_size=self.isvalue(self.size.get())
				issue_product=self.isvalue(self.product.get())
				issue_qty=self.isvalue(self.qty.get())
				issue_type=self.isvalue(self.type.get())
				remarks=self.isvalue(self.remark.get(1.0,END))
				create_by=self.username
				create_date=datetime.datetime.now().strftime('%Y/%m/%d-%H%M')

				edit_list=[issue_status,issue_from,issue_to,issue_date,issue_type,issue_size,issue_qty,issue_product,remarks,create_by,create_date]
				a=data.update('safety_shoes',eid,edit_list)
				if a:
					tkMessageBox.showinfo('Notice','Edit Success.')
					self.clearItem()
					self.get_item_list()
					self.id.set('')
					self.get_first_page()
					self.status.focus_set()	
				else:
					tkMessageBox.showinfo('Notice','plese try again.')
					self.status.focus_set()
					return
			else:
				tkMessageBox.showinfo('Notice','Please check your data.')
				self.status.focus_set()
				return

	def delItem(self):
		if self.id.get():
			a=data.delete('safety_shoes',self.id.get())
			if a:
				tkMessageBox.showinfo('Notice','Delete already.')
				self.clearItem()
				self.get_item_list()
				self.id.set('')
				self.get_first_page()
				self.status.focus_set()
			else:
				tkMessageBox.showinfo('Notice','Please try again.')
				self.status.focus_set()
				return
		else:
			tkMessageBox.showinfo('Notice','Please select the item.')
			self.status.focus_set()
			return

	def clearItem(self):
		self.status.set('')
		self.fromL.set('')
		self.toL.set('')
		self.date.set(datetime.datetime.now().strftime('%Y/%m/%d'))
		self.type.set(GET_TYPE[0])
		self.id.set('')
		self.size.set('6')
		self.qty.set('')
		self.product.set(GET_PRODUCT[0])
		self.remark.delete(1.0,END)

	def searchItem(self):
		pass

	#######################
	### PAGE MANAGEMENT ###
	#######################
	def providerpage(self):
		m=self.pages.get()
		p=m.split('/')
		if int(p[0])>1:
			n=int(p[0])-1
			new_page=str(n) + '/' + p[1]
			self.pages.set(new_page)
			new_items=self.DATALIST[((n-1)*25):(n*25)]
			for i in self.issuelist.get_children():
				self.issuelist.delete(i)
			for i in new_items:
				one_item=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['issue_type'],i['issue_size'],i['issue_qty'],i['issue_product'],i['remarks'],i['create_by'],i['create_date']]
				self.issuelist.insert('','end',values=one_item)
#				self.issuelist.insert('','end',values=i)
		else:
				tkMessageBox.showinfo('Notice','This is First page already.')
				return

	def nextpage(self):
		m=self.pages.get()
		p=m.split('/')
		if int(p[0]) >= int(p[1]):
			tkMessageBox.showinfo('Notice','this is Lastest page already.')
			return
		n=int(p[0])
		new_page=str(n+1) + '/' + p[1]
		self.pages.set(new_page)
		if int(p[0])==int(p[1]):
			new_items=self.DATALIST[(n*25):]
		else:
			new_items=self.DATALIST[(n*25):((n+1)*25-1)]
		for i in self.issuelist.get_children():
			self.issuelist.delete(i)
		for i in new_items:
			one_item=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['issue_type'],i['issue_size'],i['issue_qty'],i['issue_product'],i['remarks'],i['create_by'],i['create_date']]
			self.issuelist.insert('','end',values=one_item)


	def get_first_page(self):
		if self.DATALIST:
			self.DATALIST=[]
		if self.issuelist.get_children():
			for i in self.issuelist.get_children():
				self.issuelist.delete()
		self.get_item_list()

	#########################
	### SUPPORT FUNCTIONS ###
	#########################
		
		
	#=========== CHECK THE ENTRY VALUES =============
	def isvalue(self,value=None):
		if value:
			return value.strip().upper()
		else:
			return None

	def isstatus(self):
		if self.status.get():
			status=(self.status.get()).strip()
			if not status in GET_STATUS:
				tkMessageBox.showinfo('Notice','Please select the correct status.')
				return False
		else:		
			tkMessageBox.showinfo('Notice','Please select status.')
			return False
		return True
	def issize(self):
		if self.size.get():
			if not int(self.size.get()) in range(4,13):
				tkMessageBox.showinfo('Notice','Please select corrent size.')
				return False
		else:
			tkMessageBox.showinfo('Notice','Please select size.')
			return False
		return True	
	def isqty(self):
		if self.qty.get():
			if not self.qty.get().isdigit():
				tkMessageBox.showinfo('Notice','Please select corrent qty.')
				return False
			elif int(self.qty.get())==0:
				tkMessageBox.showinfo('Notice','Please select corrent qty. not "0".')
				return False
		else:
			tkMessageBox.showinfo('Notice','Please select qty.')
			return False
		return True	
	def istype(self):
		if self.type.get():
			if not self.type.get() in GET_TYPE:
				tkMessageBox.showinfo('Notice','Please select issue types.')
				return False
		else:
			tkMessageBox.showinfo('Notice','Please select issue types.')
			return False
		return True
	def isfromL(self):
		print "from: %s"%(self.fromL.get())
		if not self.fromL.get():
			tkMessageBox.showinfo('Notice','Please select issue from.')
			return False
	def istoL(self):
		print "to-===>"
		print "to: %s"%(self.toL.get())
		if not self.toL.get():
			tkMessageBox.showinfo('Notice','Please select issue to.')
			return False
	

	def getUI(self):
		return self

