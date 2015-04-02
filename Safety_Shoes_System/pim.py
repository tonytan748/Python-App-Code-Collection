#coding:utf-8
from editablesafetyshoesfactory import EditableSafetyShoesFactory 
from editabletshirtfactory import EditableTShirtFactory
import Tkinter
from Tkinter import *
from config import *
from login_management import LoginManagement

class PIM:
	def __init__(self):
		root=Tk()
		root.minsize(width=1200, height=700)
		root.maxsize(width=1200, height=700)

		### LOGOUT ###
#		root.protocol("WM_DELETE_WINDOW", self.logout)
		################
		### TOP MENU ###
		################
		menubar=Tkinter.Menu(root)
		productmenu=Tkinter.Menu(menubar,tearoff=0)
		productmenu.add_command(label='Product Management',command=self.add_product)
		menubar.add_cascade(label='Product Management',menu=productmenu)

		statusmenu=Tkinter.Menu(menubar,tearoff=0)
		statusmenu.add_command(label='Status Management',command=self.add_status)
		menubar.add_cascade(label='Status Management',menu=statusmenu)

#		if self.user=="admin":
#			usermenu=Tkinter.Menu(menubar,tearoff=0)
#			usermenu.add_command(label='User Management')
#			menubar.add_cascade(label='User Management',menu=usermenu)

		statusmenu=Tkinter.Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Search',menu=statusmenu)

		helpmenu=Tkinter.Menu(menubar,tearoff=0)
		helpmenu.add_command(label='About')
		helpmenu.add_command(label='Help')
		menubar.add_cascade(label='Help',menu=helpmenu)

		menubar.add_cascade(label='Exit',command=root.quit)

		root.config(menu=menubar)

		##################
		### MAIN FRAME ###
		##################
		mainFrame=Tkinter.Frame(root)
		mainFrame.master.title('SAFETY SHOES & T-SHIRT SYSTEM')

		### NAVIGATION LIST ###
		navFrame=Tkinter.Frame(mainFrame,bd=2,width=200,height=600,relief=SUNKEN)
		navFrame.pack_propagate(0)

		x=LoginManagement()
		username=x.readName()
		self.userLabel=Tkinter.Label(navFrame,text=username)

		self.safetyshoesButton=Tkinter.Button(navFrame,width=15,text='SAFETY SHOES')
		self.tshirtButton=Tkinter.Button(navFrame,width=15,text='T-SHIRT')
		self.safetyshoesButton.config(command=self.safetyshoesClicked)
		self.tshirtButton.config(command=self.tshirtClicked)
		self.userLabel.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
		self.safetyshoesButton.grid(row=1,column=0,padx=10,pady=5,stick=W+N)
		self.tshirtButton.grid(row=2,column=0,padx=10,pady=5,stick=W)
		navFrame.grid(row=0,column=0,stick=W+N)
		### MAIN FROME ###
		self.editorFrame = Tkinter.Frame(mainFrame,bd=2,width=1000,height=600, relief=SUNKEN)
		self.editorFrame.pack_propagate(0)
		self.editorFrame.grid(row=0, column=1, stick=N)
		self.editor = Tkinter.Frame(self.editorFrame)
		self.editor.grid()
		self.safetyshoesClicked()

		mainFrame.pack()
		mainFrame.mainloop()

	def safetyshoesClicked(self):
		safetyshoes=EditableSafetyShoesFactory().createEditable(self.editorFrame)
		self.editor.grid_remove()
		self.editor=safetyshoes.getEditor()
		self.editor.getUI().grid()
		self.safetyshoesButton.configure(bg='blue')
		self.tshirtButton.configure(bg='grey')

	def tshirtClicked(self):
		tshirt=EditableTShirtFactory().createEditable(self.editorFrame)
		self.editor.grid_remove()
		self.editor=tshirt.getEditor()
		self.editor.getUI().grid()
		self.safetyshoesButton.configure(bg='grey')
		self.tshirtButton.configure(bg='blue')


	########################
	### TOP MENU COMMAND ###
	########################
	def add_product(self):
		pass
	def add_status(self):
		pass


	def logout(self):
		x=LoginManagement()
		x.removeFile()
		sys.exit(0)

if (__name__ == "__main__"):
	app = PIM()
