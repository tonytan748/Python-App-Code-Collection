#-*-coding=utf-8-*-
import os,sys
from Tkinter import *
import tkMessageBox
import ttk
import datetime
import data

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
STATUS=os.path.join(FILEPATH,'status.txt')
PRODUCTNAME=os.path.join(FILEPATH,'productname.txt')

GET_ITEMS=data.get_data()
GET_STATUS=data.get_items(STATUS)
GET_PRODUCTNAME=data.get_items(PRODUCTNAME)
GET_NAMES=data.get_name_list()

localkinds=['OFFICE','STORE']

class ReportCenter(object):
        def __init__(self,master,info='Report Management'):
                self.ma=master
                self.topline=Frame(self.ma)
		#========name list=========
                frame1=Frame(self.topline,bd=1)
                Label(frame1,text='Employee Name').grid(row=0,column=0,sticky=W)
                
                self.getnamelist=[i[1]+'  '+i[0] for i in GET_NAMES]
                self.namelist=ttk.Combobox(frame1)
                self.namelist['values']=tuple(self.getnamelist)
                self.namelist['width']=25
                self.namelist.bind('<Return>',self.getFromName)
                self.namelist.grid(row=0,column=1,sticky=W)                

                self.allemployee=IntVar()
                c=Checkbutton(frame1,text='All Employee',variable=self.allemployee,command=self.select_all_employee)
                c.grid(row=1,column=0,columnspan=2,sticky=W)

                self.employeebtn=Button(frame1,text="Search",command=self.get_employee_result)
                self.employeebtn.grid(row=1,column=1,sticky=W)
                #frame1.grid(row=0,column=0)
                frame1.pack(fill=X,side=LEFT)
                
                #========production name=======
                frame2=Frame(self.topline,bd=1,background='red')
                Label(frame2,text='Production Name',bg="red").grid(row=0,column=0,sticky=W)

                self.getprolist=[i for i in GET_PRODUCTNAME]
                self.productlist=ttk.Combobox(frame2)
                self.productlist['values']=tuple(self.getprolist)
                self.productlist['width']=25
                self.productlist.grid(row=1,column=0,sticky=W)
                #frame2.grid(row=0,column=1)
                frame2.pack(fill=X,side=LEFT)
                
                #========location=============
                frame3=Frame(self.topline,bd=1,background='blue')
                self.v1=IntVar()
                self.v1.set(1)
                self.check1=Checkbutton(frame3,text=localkinds[0],variable=self.v1)
                self.check1.pack(fill=X)
                self.v2=IntVar()
                self.v2.set(1)
                self.check2=Checkbutton(frame3,text=localkinds[1],variable=self.v2)
                self.check2.pack(fill=X)
                #frame3.grid(row=0,column=2)
                frame3.pack(fill=X,side=LEFT)
                
                #=========search Button==========
                self.searchbtn=Button(self.topline,text='Search',command=self.search)
                #self.searchbtn.grid(row=0,column=3,sticky=W)
                self.searchbtn.pack(fill=X,side=LEFT)

                self.topline.pack(fill=X)
                
                #=========result list==========
                listf=Frame(self.ma,bd=1)
                bary1=Scrollbar(listf)
                bary1.pack(side=RIGHT,fill=Y)
                self.listlabel=Text(listf,width=157,height=6)
                self.listlabel.pack(side=LEFT,fill=BOTH)
                bary1.config(command=self.listlabel.yview)
                self.listlabel.config(yscrollcommand=bary1.set)
                #listf.grid(row=1,column=0,columnspan=4,sticky=W)
                listf.pack(fill=X)
                
                self.listlabel.insert(0.0,'test\n1\t2\t3\t4\n111\t222\t333\t444\n111\t222\t333\t444\n111\t222\t333\t444\n111\t222\t333\t444\n111\t222\t333\t444\n111\t222\t333\t444\n111\t222\t333\t444')

                #=========search list============
                issue_list=['ID','Status','From Location','To Location','Date','Product Name','Size','Qty','Remark','Create By','Create Date']
                listbar=Frame(self.ma)

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
                #listbar.grid(row=2,column=0,columnspan=4,sticky=W)
                listbar.pack(fill=X)

        def get_employee_result(self):
                if self.namelist.get() and self.allemployee.get()==1:
                        tkMessageBox.showinfo('Notice','Please select your employee.')
                        return
                res=[]
                if self.namelist.get():
                        resultlist='Search ' + self.namelist.get() + '\nReceived\tReturn\tBalance\n'
                        a=self.getNameQtyInfo(self.namelist.get())
                        resultlist = resultlist + a[0]
                        res.extend(a[1])
                else:
                        resultlist='Search All Employee\n'
                        resultlist=resultlist + 'Employee Name\tReceived Qty\tReturn Qty\tBalance\n'
                        x=(i[1] + '  ' + i[0] for i in GET_NAMES)
                        for i in x:
                                einfo=self.getNameQtyInfo(i)
                                resultlist=resultlist + einfo[0]
                                res.extend(einfo[1])
                if res:
                        self.listlabel.insert(0.0,resultlist)
                        for i in self.issuelist.get_children():
                                self.issuelist.delete(i)
                        if len(res)<25:
                                for i in range(len(res)):
                                        s=[str(i['id']),str(i['issue_status']),str(i['issue_from']),str(i['issue_to']),str(i['issue_date']),str(i['product_name']),str(i['size']),str(i['qty']),str(i['remarks']),str(i['create_by']),str(i['create_date'])]
                                        self.issuelist.insert('','end',values=s)
                        else:
                                for i in range(0,25):
                                        s=[str(i['id']),str(i['issue_status']),str(i['issue_from']),str(i['issue_to']),str(i['issue_date']),str(i['product_name']),str(i['size']),str(i['qty']),str(i['remarks']),str(i['create_by']),str(i['create_date'])]
                                        self.issuelist.insert('','end',values=s)
                        
        def getNameQtyInfo(self,name):
                if name:
                        l=[]
                        itemlist=(i for i in GET_ITEMS if i['issue_status'].startswith('EMPLOYEE') or i['issue_status'].endswith('EMPLOYEE'))
                        issueresult=list(int(i['qty']) for i in itemlist if i['issue_to']==self.namelist.get())
                        returnresult=list(int(i['qty']) for i in itemlist if i['issue_from']==self.namelist.get())
                        l.extend(issueresult)
                        l.extend(returnresult)
                        i=sum(issueresult)
                        r=sum(returnresult)
                        b=i-r
                        resultlist=name + '\t' + str(i) + '\t' + str(r) + '\t' + str(b) + '\n'
                        return (resultlist,l)
        
        def getIssueItem(self,event):
                pass
        def search(self):
                #check production name....
                print GET_ITEMS
                if self.productlist.get():
                        itemlist=(i for i in itemlist if i['product_name']==self.productlist.get())
                if self.v1.get()==1 and self.v2.get()==1:
                        pass
        def getFromName(self,event):
                if self.namelist.get():
                        a=[i for i in GET_NAMES if self.namelist.get().upper() in i[1].strip()]
                        if a:
                                fullname=a[0][1]+ '  ' + a[0][0]
                                self.namelist.delete(0,END)
                                self.namelist.insert(0,fullname)
        def select_all_employee(self):
                if self.allemployee:
                        self.namelist.set('')
                #elif self.allemployee=0:
                        
                                
def main():
        root=Tk()
        product_name=ReportCenter(root)
        mainloop()
main()
if __name__=='__main__':
        main()
	
