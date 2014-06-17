#-*-coding=utf-8-*-
import os,sys
from Tkinter import *
import tkMessageBox
import ttk
import datetime
import data


from productname import main as promain
from status import main as statusmain

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
USER=os.path.join(FILEPATH,'user.txt')
STATUS=os.path.join(FILEPATH,'status.txt')
PRODUCTNAME=os.path.join(FILEPATH,'productname.txt')

GET_ITEMS=data.get_data()
GET_STATUS=data.get_items(STATUS)
GET_PRODUCTNAME=data.get_items(PRODUCTNAME)
GET_USER=data.get_items(USER)
GET_NAMES=data.get_name_list()


DATAFILE=os.path.join(FILEPATH,'safety.db')
if os.path.exists(DATAFILE):
	print 'a'
	data.create_table()

class loginPage(object):
	def __init__(self,master,info='Safety Shoes System'):
		self.master=master
		self.mainlabel=Label(master,text=info,justify=CENTER)
		self.mainlabel.grid(row=0,columnspan=3)

		self.user=Label(master,text='Username',borderwidth=2)
		self.user.grid(row=1,sticky=W)

		self.pwd=Label(master,text='Password',borderwidth=2)
		self.pwd.grid(row=2,sticky=W)

		self.attn=[i.split(',')[0] for i in GET_USER]
		self.userEntry=ttk.Combobox(master)
		self.userEntry['values']=tuple(self.attn)
		self.userEntry.grid(row=1,column=1,columnspan=2)
		self.userEntry.focus_set()

		self.pwdEntry=Entry(master,show='*')
		self.pwdEntry.bind('<Return>',self.loginit)
		self.pwdEntry.grid(row=2,column=1,columnspan=2)

		self.loginButton=Button(master,text='Login',borderwidth=2,command=self.login)
		self.loginButton.grid(row=3,column=1)

		self.cleanButton=Button(master,text='Clean',borderwidth=2,command=self.clear)
		self.cleanButton.grid(row=3,column=2)

	def login(self):
		self.username=self.userEntry.get().strip()
		self.passwd=self.pwdEntry.get().strip()

		if len(self.username) == 0 or len(self.passwd) ==0 or not self.username in 	self.attn:
			tkMessageBox.showinfo('Notice','please check your username')
			self.clear()
			self.userEntry.focus_set()
			return
		else:
			pw=[i.split(',')[1] for i in GET_USER if i.split(',')[0]==self.username]
			p=pw[0].strip('')
			if not self.passwd == p:
				tkMessageBox.showinfo('Notice','Please check your username')
				self.clear()
				self.userEntry.focus_set()
				return
		self.connect()

	def loginit(self,event):
		self.login()

	def connect(self):
		self.username=self.userEntry.get().strip()
		self.mainframe=MainFrame(self.master,self.username)

	def clear(self):
		self.userEntry.delete(0,END)
		self.pwdEntry.delete(0,END)


class MainFrame(object):
	def __init__(self,master,user=''):
		self.user=user
		self.DATALIST=None
		self.mas=Toplevel(master)

		menubar=Menu(self.mas)
		productmenu=Menu(menubar,tearoff=0)
		productmenu.add_command(label='Product Management',command=self.add_product)
		menubar.add_cascade(label='Product Management',menu=productmenu)

		statusmenu=Menu(menubar,tearoff=0)
		statusmenu.add_command(label='Status Management',command=self.add_status)
		menubar.add_cascade(label='Status Management',menu=statusmenu)

		statusmenu=Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Search',menu=statusmenu)

		helpmenu=Menu(menubar,tearoff=0)
		helpmenu.add_command(label='About')
		helpmenu.add_command(label='Help')
		menubar.add_cascade(label='Help',menu=helpmenu)

		menubar.add_cascade(label='Exit',command=master.quit)

		self.mas['menu']=menubar

		toolbar=Frame(self.mas,bd=1,relief=RAISED)
		Label(toolbar,text="STATUS").grid(row=0,column=0,sticky=W)
		Label(toolbar,text='DATE').grid(row=0,column=2,sticky=W)
		Label(toolbar,text='PRODUCT NAME').grid(row=0,column=4,sticky=W)
		Label(toolbar,text='REMARK').grid(row=0,column=8,sticky=W)

		Label(toolbar,text='FROM').grid(row=1,column=0,sticky=W)
		Label(toolbar,text='TO').grid(row=1,column=2,sticky=W)
		Label(toolbar,text='SIZE').grid(row=1,column=4,sticky=W)
		Label(toolbar,text='QTY').grid(row=1,column=6,sticky=W)

		#======STATUS======
		statuslist=[i for i in GET_STATUS]
		self.status=ttk.Combobox(toolbar)
		self.status['values']=tuple(statuslist)
		self.status['width']=25
		self.status.grid(row=0,column=1,sticky=W+N)
		#=====DATE======
		self.date=StringVar()
		self.getdate=Entry(toolbar,textvariable=self.date).grid(row=0,column=3,sticky=W+N)
		self.date.set(datetime.datetime.now().strftime('%Y/%m/%d'))
		#========PRODUCT NAME==========
		productlist=[i for i in GET_PRODUCTNAME]
		self.product=ttk.Combobox(toolbar)
		self.product['values']=tuple(productlist)
		self.product['width']=25
		self.product.grid(row=0,column=5,columnspan=3,sticky=W+N)
		#=========ID==========
		self.id=StringVar()
		Label(toolbar,textvariable=self.id).grid(row=1,column=8,sticky=W)
		self.id.set('')
		#========ISSUE FROM========
		fromlocal=[i[1]+'  '+i[0] for i in GET_NAMES]
		self.fromL=ttk.Combobox(toolbar)
		self.fromL['values']=tuple(fromlocal)
		self.fromL['width']=25
		self.fromL.bind('<Return>',self.getFromName)
		self.fromL.grid(row=1,column=1,sticky=W+N)
		#========ISSUE TO========
		self.toL=ttk.Combobox(toolbar)
		self.toL['values']=tuple(fromlocal)
		self.toL['width']=25
		self.toL.bind('<Return>',self.getToName)
		self.toL.grid(row=1,column=3,sticky=W+N)
		#========SIZE==========
		size=range(4,14)
		self.size=ttk.Combobox(toolbar)
		self.size['values']=tuple(size)
		self.size['width']=10
		self.size.grid(row=1,column=5,sticky=W)
		#=========QTY=========
		self.qty=StringVar()
		self.getqty=Entry(toolbar,textvariable=self.qty,width=8)
		self.getqty.grid(row=1,column=7,sticky=W)
		#========REMARK===========
		f1=Frame(toolbar)
		bary1=Scrollbar(f1)
		bary1.pack(side=RIGHT,fill=Y)
		self.remark=Text(f1,width=20,height=2)
		self.remark.pack(side=LEFT,fill=BOTH)
		bary1.config(command=self.remark.yview)
		self.remark.config(yscrollcommand=bary1.set)
		f1.grid(row=0,column=9,rowspan=2,sticky=W+N)
		#=========buttons==========
		toolbar.pack(side=TOP,fill=X)
		
		btnbar=Frame(self.mas)
		self.addbtn=Button(btnbar,text='ADD',command=self.addItem,width=10).grid(row=0,column=0,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=1)
		self.editbtn=Button(btnbar,text='EDIT',command=self.editItem,width=10).grid(row=0,column=2,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=3)
		self.delbtn=Button(btnbar,text='DELETE',command=self.delItem,width=10).grid(row=0,column=4,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=5)
		self.clear=Button(btnbar,text='CLEAN',command=self.clearItem,width=10).grid(row=0,column=6,sticky=W)
		Label(btnbar,width=5).grid(row=0,column=7)
		self.search=Button(btnbar,text='SEARCH',command=self.searchItem,width=10).grid(row=0,column=8,sticky=W)
		btnbar.pack(side=TOP,fill=X,pady=3)
		
		#=========ISSUE LIST============
		issue_list=['ID','Status','From Location','To Location','Date','Product Name','Size','Qty','Remark','Create By','Create Date']
		listbar=Frame(self.mas)

		bary2=Scrollbar(listbar)
		bary2.pack(side=RIGHT,fill=Y)
		barx2=Scrollbar(listbar,orient=HORIZONTAL)
		barx2.pack(side=BOTTOM,fill=X)

		self.issuelist=ttk.Treeview(listbar,columns=issue_list)
		self.issuelist.column(column='#0',width=0,stretch=False)
		for i in range(len(issue_list)):
			self.issuelist.heading(i,text=issue_list[i])
			self.issuelist.column(i,width=100)
		self.issuelist.column(0,width=30)
		self.issuelist.column(1,width=130)
		self.issuelist.column(2,width=200)	
		self.issuelist.column(3,width=200)
		self.issuelist['height']=20
		self.issuelist.bind('<<TreeviewSelect>>',self.getIssueItem)
		self.issuelist.pack(side=LEFT,fill=BOTH)

		barx2.config(command=self.issuelist.xview)
		bary2.config(command=self.issuelist.yview)

		self.issuelist.config(xscrollcommand=barx2.set,yscrollcommand=bary2)
		listbar.pack(fill=X)
		
		#========PAGES MANAGEMENT==========
		pagebar=Frame(self.mas)
		self.providerbtn=Button(pagebar,text="PROVIDER",command=self.providerpage).pack(side=LEFT,padx=5)
		self.pages=StringVar()
		self.page_pages=Label(pagebar,textvariable=self.pages).pack(side=LEFT,padx=5)
		self.pages.set('1/1')
		self.nextbar=Button(pagebar,text='Next',command=self.nextpage).pack(side=LEFT,padx=5)
		pagebar.pack(fill=X)
		
		self.get_item_list()
#=======edit from item and to item=========	
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

#======get item list=========
	def get_item_list(self):
		self.DATALIST=[]
		if self.issuelist.get_children():
			for i in self.issuelist.get_children():
				self.issuelist.delete(i)
		m=data.get_data()
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
					x=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['product_name'],i['size'],i['qty'],i['remarks'],i['create_by'],i['create_date']]
					self.issuelist.insert('','end',values=x)
			else:
				self.pages.set('1/1')
				for i in m:
					x=[i['id'],i['issue_status'],i['issue_from'],i['issue_to'],i['issue_date'],i['product_name'],i['size'],i['qty'],i['remarks'],i['create_by'],i['create_date']]
					self.issuelist.insert('','end',values=x)

#=======button============
	def addItem(self):
		if self.id.get():
			tkMessageBox.showinfo('Notice','Please try again.')
			return
		if not self.isstatus():
			self.status.focus_set()
			return False
		if not self.issize():
			self.size.focus_set()
			return False
		if not self.isqty():
			self.getqty.focus_set()
			return False
		issue_status=self.isvalue(self.status.get())
		issue_from=self.isvalue(self.fromL.get())
		issue_to=self.isvalue(self.toL.get())
		issue_date=self.isvalue(self.date.get())
		size=self.isvalue(self.size.get())
		product_name=self.isvalue(self.product.get())
		qty=self.isvalue(self.qty.get())
		remarks=self.isvalue(self.remark.get(1.0,END))
		create_by=self.user
		create_date=datetime.datetime.now().strftime('%Y%m%d-%MH%M')

		add_list=[issue_from,issue_to,product_name,size,qty,issue_date,issue_status,remarks,create_by,create_date]
		a=data.add(add_list)
		if a:
			tkMessageBox.showinfo('Notice','Add Success.')
			self.clearItem()
			self.id.set('')
			self.get_first_page()
			self.status.focus_set()
		else:
			tkMessageBox.showinfo('Notice','please try again.')
			self.status.focus_set()
			return

	def editItem(self):
		if not self.isstatus():
			self.status.focus_set()
			return False
		if not self.issize():
			self.size.focus_set()
			return False
		if not self.isqty():
			self.getqty.focus_get()
			return False
		if self.id.get():
			item_id= int(self.id.get())
			print item_id
			m=list(i['id'] for i in GET_ITEMS)
			print m
			if item_id in m:
				id=self.id.get()
				issue_status=self.isvalue(self.status.get())
				issue_from=self.isvalue(self.fromL.get())
				issue_to=self.isvalue(self.toL.get())
				issue_date=self.isvalue(self.date.get())
				size=self.isvalue(self.size.get())
				product_name=self.isvalue(self.product.get())
				qty=self.isvalue(self.qty.get())
				remarks=self.isvalue(self.remark.get(1.0,END))
				create_by=self.user
				create_date=datetime.datetime.now().strftime('%Y%m%d-%MH%M')

				edit_list=[issue_from,issue_to,product_name,size,qty,issue_date,issue_status,remarks,create_by,create_date]
				a=data.update(id,edit_list)
				if a:
					tkMessageBox.showinfo('Notice','Edit Success.')
					self.clearItem()
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
			a=data.delete(self.id.get())
			if a:
				tkMessageBox.showinfo('Notice','Delete already.')
				self.clearItem()
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
		self.date.set(datetime.datetime.now().strftime('%Y/%m/%d'))
		self.product.set('')
		self.fromL.set('')
		self.toL.set('')
		self.size.set('')
		self.qty.set('')
		self.remark.delete(1.0,END)
		self.id.set('')
	def searchItem(self):
		pass

	def isvalue(self,value=None):
		if value:
			return value.strip().upper()
		else:
			return None

	def isstatus(self):
		if self.status.get():
			status=self.status.get()
			print status
			print GET_STATUS
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
		else:
			tkMessageBox.showinfo('Notice','Please select qty.')
			return False
		return True	
			
	def getIssueItem(self,event):
		self.clearItem()
		self.id.set('')
		m=self.issuelist.selection()
		print m
		if m:
			x=self.issuelist.item(m)['values']
			print x
			s_list=dict(id=x[0],status=x[1],fromL=x[2],toL=x[3],date=x[4],product=x[5],size=x[6],qty=x[7],remark=x[8],create_by=x[9],create_date=x[10])
			self.status.set(s_list['status'])
			self.fromL.set(s_list['fromL'])
			self.toL.set(s_list['toL'])
			self.date.set(s_list['date'])
			self.product.insert(0,s_list['product'])
			self.size.set(s_list['size'])
			self.qty.set(s_list['qty'])
			self.id.set(s_list['id'])
			self.remark.insert(0.0,s_list['remark'])


#========PAGE MANAGEMENT=======
	def providerpage(self):
		m=self.pages.get()
		p=m.split('/')
		if int(p[0])>1:
			n=int(p[0])-1
			new_page=str(n) + '/' + p[1]
			self.pages.set(new_page)
			new_items=self.DATALIST[((n-1)*25):(n*25-1)]
			for i in self.issuelist.get_children():
				self.issuelist.delete(i)
			for i in new_items:
				self.issuelist.insert('','end',values=i)

	def nextpage(self):
		m=self.pages.get()
		p=m.split('/')
		if int(p[0]) > int(p[1]):
			return
		n=int(p[0])
		new_page=str(n+1) + '/' + p[1]
		self.pages.set(new_page)
		new_items=self.DATALIST[(n*25):((n+1)*25-1)]
		for i in self.issuelist.get_children():
			self.issuelist.delete()
		for i in new_items:
			self.issuelist.insert('','end',values=i)

	def get_first_page(self):
		if self.DATALIST:
			self.DATALIST=[]
		if self.issuelist.get_children():
			for i in self.issuelist.get_children():
				self.issuelist.delete()
		self.get_item_list()		
	
#=========Menu===========
	def add_product(self):
		self.add_product=promain()
		
	def add_status(self):
		self.add_status=statusmain()

def main():
        root=Tk()
        log=loginPage(root)
        mainloop()
main()
if __name__=='__main__':
	root=Tk()
	log=loginPage(root)
	mainloop()
