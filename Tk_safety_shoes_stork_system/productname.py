
import os,sys
from Tkinter import *
import tkMessageBox
import ttk
import datetime
import data

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
PRODUCTNAME=os.path.join(FILEPATH,'productname.txt')
GET_PRODUCTNAME=data.get_items(PRODUCTNAME)

class ProductManagement(object):
	def __init__(self,master,info='Product Management'):
		self.ma=master

		Label(self.ma,text="Product Name:").grid(row=0,column=0,sticky=W)
		
		self.productlist=[i for i in GET_PRODUCTNAME]
		self.product=ttk.Combobox(self.ma)
		self.product['values']=tuple(self.productlist)
		self.product['width']=25
		self.product.grid(row=0,column=1,sticky=W)

		self.add=Button(self.ma,text='ADD',command=self.product_add)
		self.add.grid(row=1,column=0,sticky=W)

		self.delete=Button(self.ma,text="DELETE",command=self.product_del)
		self.delete.grid(row=1,column=1,sticky=W)
	def product_add(self):
		p=self.product.get()
		if p:
			if p in self.productlist:
				tkMessageBox.showinfo('Notice','This product name is created already.')
				return
			else:
				data.add_items(PRODUCTNAME,p)
				tkMessageBox.showinfo('Notice','Add success.')
	def product_del(self):	
		p=self.product.get()
		if p:
			if p in self.productlist:
				data.del_items(PRODUCTNAME,p)
				tkMessageBox.showinfo('Notice','Delete success.')
			else:
				tkMessageBox.showinfo('Notice','This one is not in list.')
				return 
def main():
	root=Tk()
	product_name=ProductManagement(root)
	mainloop()
	