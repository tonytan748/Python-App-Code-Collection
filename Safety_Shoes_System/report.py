#coding:utf-8
import os,sys
import csv
import tkMessageBox
from Tkinter import *
from tkFileDialog import *

from config_safetyshoes import *
from config_tshirt import *
from config import *

class Report:
	def __init__(self,table_name):
		self.table_name=table_name

	def safetyshoes_lend_single(self,ec):
		x={}
		x['ec']=ec.upper()
		for i in GET_NAMES:
			if i[1]==x['ec']:
				x['name']=i[0].strip()
		x['sum']=0
		for i in range(4,14):
			x[str(i)]=0
		m=[i for i in data.get_data('safety_shoes',SAFETY_SHOES) if (((i['issue_to']).split(' '))[0]==x['ec'] and ((i['issue_type']).upper() in [j for j in GET_ISSUE if j.upper()!="ISSUE"]))]
		for a in m:
			if str(a['issue_size']) in map(str,range(4,14)):
				if a['issue_type']=="ISSUEED":
					x[str(a['issue_size'])]+=int(a['issue_qty'])
					x['sum']+=int(a['issue_qty'])
				elif a['issue_type']=="RETURNED":
					x[str(a['issue_size'])]-=int(a['issue_qty'])
					x['sum']-=int(a['issue_qty'])
				x['remarks']=''
		return x

	def safetyshoes_issue_single(self,ec):
		x={}
		x['ec']=ec.upper()
		for i in GET_NAMES:
			if i[1]==x['ec']:
				x['name']=i[0].strip()
		x['sum']=0
		for i in range(4,14):
			x[str(i)]=0

		print data.get_data('safety_shoes',SAFETY_SHOES)
		print SAFETY_SHOES
		m=[i for i in data.get_data('safety_shoes',SAFETY_SHOES) if (((i['issue_to']).split(' '))[0]==x['ec'] and (((i['issue_status']).split(' '))[2]).upper()=="EMPLOYEE")]
		for a in m:
			if str(a['issue_size']) in map(str,range(4,14)):
				x[str(a['issue_size'])]+=int(a['issue_qty'])
				x['sum']+=int(a['issue_qty'])
				x['remarks']=''
		return x

	def calculate_safetyshoes(self,whichone):
		name_item=[item[1] for item in GET_NAMES if (len(item[1])==7)]
		if whichone=="lend":
			for i in map(self.safetyshoes_lend_single,name_item):
				item=[i['name'],i['ec'],i['4'],i['5'],i['6'],i['7'],i['8'],i['9'],i['10'],i['11'],i['12'],i['13'],i['sum'],'']
				yield item
		else:
			for i in map(self.safetyshoes_issue_single,name_item):
				item=[i['name'],i['ec'],i['4'],i['5'],i['6'],i['7'],i['8'],i['9'],i['10'],i['11'],i['12'],i['13'],i['sum'],'']
				yield item

	def output_safetyshoes(self,report_path,whichone):
		head_content=self.report_head('safetyshoes',whichone)
		if head_content:
			dict_write=csv.writer(open(report_path,'wb'))
			dict_write.writerow(head_content['title'])
			dict_write.writerow(head_content['subtitle'])
			dict_write.writerow(head_content['heads'])

			for item in self.calculate_safetyshoes(whichone):
				dict_write.writerow(item)


	def safetyshoes_get_stock(self,pro_name=None,local=None):
		data.get_data('safety_shoes',SAFETY_SHOES)
		lin=[i for i in data.get_data('safety_shoes',SAFETY_SHOES) if ((((i['issue_status']).split(' '))[2]).upper()==local.upper())]
		lout=[i for i in data.get_data('safety_shoes',SAFETY_SHOES) if ((((i['issue_status']).split(' '))[1]).upper()==local.upper())]
		pro_list=[]
		pro_list.append(pro_name.upper())
		s=0
		for i in range(4,14):
			x1=[int(i['issue_qty']) for i in lin if(i['issue_size']==str(i))]
			sum1=sum(x1)
			x2=[int(i['issue_qty']) for i in lout if(i['issue_size']==str(i))]
			sum2=sum(x2)
			pro_list.append(str(int(suml)-int(sum2)))
			s+=int(suml)-int(sum2)
		pro_list.append(str(s))
		return pro_list

	def stock_safetyshoes(self,report_path):
		dict_write=csv.writer(open(report_path,'wb'))
		dict_write.writerow('SAFETY SHOES STOCK REPORT')

		xx1=[]
		xx1.append('STORE')
		for i in range(4,14):
			xx1.append('')
		xx1.append('')
		xx1.append('OFFICE')
		for i in range(4,14):
			xx1.append('')
		xx1.append('')
		dict_write.writerow(xx1)

		xx=[]
		for j in range(0,2):
			xx.append('')
			for i in range(4,14):
				xx.append(str(i))
			xx.append('TOTAL')

		dict_write.writerow(xx)

		for i in GET_PRODUCT:
			name=GET_PRODUCT[i]
			stock_list=self.safetyshoes_get_stock(pro_name,'STORE')
			office_list=self.safetyshoes_get_stock(pro_name,'OFFICE')
			m=[]
			m.append(stock_list)
			m.append(office_list)
			dict_write.writerow(m)



	def tshirt_lend_single(self,ec):
		x={}
		x['ec']=ec.upper()
		for i in GET_NAMES:
			if i[1]==x['ec']:
				x['name']=i[0].strip()
		x['sum']=0
		for i in GET_SIZE:
			x[str(i)]=0
		m=[i for i in data.get_data('tshirt',TSHIRT) if (((i['issue_to']).split(' '))[0]==x['ec'] and ((i['issue_type']).upper() in [j for j in GET_ISSUE if j.upper()!="ISSUE"]))]
		for a in m:
			print a
			if str(a['issue_size']) in GET_SIZE:
				if a['issue_type']=="RETURN":
					x[str(a['issue_size'])]=int(x[str(a['issue_size'])])+int(a['issue_qty'])
					x['sum']=int(x['sum'])+int(a['issue_qty'])
				elif a['issue_type']=="LEND":
					x[str(a['issue_size'])]=int(x[str(a['issue_size'])])+int(a['issue_qty'])
					x['sum']=int(x['sum'])+int(a['issue_qty'])
				x['remarks']=''
		return x
	def tshirt_issue_single(self,ec):
		x={}
		x['ec']=ec.upper()
		for i in GET_NAMES:
			if i[1]==x['ec']:
				x['name']=i[0].strip()
		x['sum']=0
		for i in GET_SIZE:
			x[str(i)]=0
		m=[i for i in data.get_data('tshirt',TSHIRT) if (((i['issue_to']).split(' '))[0]==x['ec'] and ((i['issue_type']).upper()=="ISSUE"))]
#		print len(data.get_data('tshirt',TSHIRT))
		for a in m:
#			print "a:   %s"%a
			if str(a['issue_size']) in GET_SIZE:
				x[str(a['issue_size'])]=int(x[str(a['issue_size'])])+int(a['issue_qty'])
				x['sum']=int(x['sum'])+int(a['issue_qty'])
				x['remarks']=''
#		print "==>   %s"%x
		return x

	def calculate_tshirt(self,whichone):
		name_item=[item[1] for item in GET_NAMES if (len(item[1])==7)]
		if whichone=="lend":
			for i in map(self.tshirt_lend_single,name_item):
				item=[i['name'],i['ec'],i['XS'],i['S'],i['M'],i['L'],i['XL'],i['sum'],'']
				yield item
		else:
			for i in map(self.tshirt_issue_single,name_item):
				item=[i['name'],i['ec'],i['XS'],i['S'],i['M'],i['L'],i['XL'],i['sum'],'']
				yield item

	def output_tshirt(self,report_path,whichone):
		head_content=self.report_head('tshirt',whichone)
		if head_content:
			dict_write=csv.writer(open(report_path,'wb'))
			dict_write.writerow(head_content['title'])
			dict_write.writerow(head_content['subtitle'])
			dict_write.writerow(head_content['heads'])

			for item in self.calculate_tshirt(whichone):
				dict_write.writerow(item)

	def tshirt_get_stock(self,pro_name=None,local=None):
		data.get_data('tshirt',TSHIRT)
		lin=[i for i in data.get_data('tshirt',TSHIRT) if ((((i['issue_status']).split(' '))[2]).upper()==local.upper())]
		lout=[i for i in data.get_data('tshirt',TSHIRT) if ((((i['issue_status']).split(' '))[1]).upper()==local.upper())]
		pro_list=[]
		pro_list.append(pro_name.upper())
		s=0
		for i in GET_SIZE:
			x1=[int(i['issue_qty']) for i in lin if(i['issue_size']==str(i))]
			sum1=sum(x1)
			x2=[int(i['issue_qty']) for i in lout if(i['issue_size']==str(i))]
			sum2=sum(x2)
			pro_list.append(str(int(suml)-int(sum2)))
			s+=int(suml)-int(sum2)
		pro_list.append(str(s))
		return pro_list

	def stock_tshirt(self,report_path):
		dict_write=csv.writer(open(report_path,'wb'))
		dict_write.writerow('TSHIRT STOCK REPORT')


		xx1=[]
		xx1.append('STORE')
		for i in GET_SIZE:
			xx1.append('')
		xx1.append('')
		xx1.append('OFFICE')
		for i in GET_SIZE:
			xx1.append('')
		xx1.append('')
		dict_write.writerow(xx1)

#		dict_write.writerow(['STORE',,,,,,,,,,,'OFFICE',,,,,,,])

		xx=[]
		for j in range(0,2):
			xx.append('')
			for i in GET_SIZE:
				xx.append(str(i))
			xx.append('TOTAL')

		dict_write.writerow(xx)

		for i in GET_PRODUCT:
			name=GET_PRODUCT[i]
			stock_list=self.tshirt_get_stock(pro_name,'STORE')
			office_list=self.tshirt_get_stock(pro_name,'OFFICE')
			m=[]
			m.append(stock_list)
			m.append(office_list)
			dict_write.writerow(m)


	def safety_shoes_report(self,itype):
		name=os.path.join(FILEPATH,'safety_shoes_report.csv')
		temp_issue_worker_report=asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,parent=self.mas,title='Save')

		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		self.output_safetyshoes(temp_issue_worker_report,itype)
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	def safety_shoes_stock_report(self):
		name=os.path.join(FILEPATH,'safety_shoes_stock_report.csv')
		temp_issue_worker_report=asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,parent=self.mas,title='Save')
		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		self.stock_safetyshoes(temp_issue_worker_report,itype)
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	def tshirt_lend_report(self,itype):
		name=os.path.join(FILEPATH,'tshirt_lend_report.csv')
		temp_issue_worker_report=asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,parent=self.mas,title='Save')

		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		self.output_tshirt(temp_issue_worker_report,itype)
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')

	def tshirt_stock_report(self):
		name=os.path.join(FILEPATH,'tshirt_stock_report.csv')
		temp_issue_worker_report=asksaveasfilename(defaultextension='.csv',filetypes=[('Excel Files','*.csv')],initialdir='C:\\',initialfile=name,parent=self.mas,title='Save')
		if os.path.exists(temp_issue_worker_report):
			os.remove(temp_issue_worker_report)
		self.stock_tshirt(temp_issue_worker_report,itype)
		print "finished..."
		tkMessageBox.showinfo('Notice','The Report saved already!')



	def report_head(self,t_name,whichone):
		x={}
		if t_name=="safetyshoes":
			if whichone=="lend":
				x['title']=["SAFETY SHOES LEND REPORT"]
				x['subtitle']=[""]
				x['heads']=['NAME','EMPLOYEE CODE','4','5','6','7','8','9','10','11','12','13','Total Balance','Remarks']
				x['item']=['name','ec','4','5','6','7','8','9','10','11','12','13','sum','']

			elif whichone=="issue":
				x['title']=["SAFETY SHOES DISTRIBUTION (CONTROL) LIST"]
				x['subtitle']=["NOTE : 1 PAIR EVERY 6 MONTHS"]
				x['heads']=['NAME','EMPLOYEE CODE','4','5','6','7','8','9','10','11','12','13','Total Qty','Remarks']
				x['item']=['name','ec','4','5','6','7','8','9','10','11','12','13','sum','']

			elif whichone=="stock":
				x['title']=["SAFETY SHOES STOCK REPORT"]
				x['subtitle']=[""]
				x['heads']=['LOCATION','4','5','6','7','8','9','10','11','12','13','Total Qty','Remarks']
				x['item']=['location','4','5','6','7','8','9','10','11','12','13','sum','']

		elif t_name=="tshirt":
			if whichone=="lend":
				x['title']=["TSHIRT LEND REPORT"]
				x['subtitle']=[""]
				x['heads']=['NAME','EMPLOYEE CODE','XS','S','M','L','XL','Total Qty','Remarks']
				x['item']=['name','ec','XS','S','M','L','XL','sum','']

			elif whichone=="issue":
				x['title']=["TSHIRT DISTRIBUTION (CONTROL) LIST"]
				x['subtitle']=["NOTE : 1 PAIR EVERY 6 MONTHS"]
				x['heads']=['NAME','EMPLOYEE CODE','XS','S','M','L','XL','Total Qty','Remarks']
				x['item']=['name','ec','XS','S','M','L','XL','sum','']

			elif whichone=="stock":
				x['title']=["TSHIRT STOCK REPORT"]
				x['subtitle']=["NOTE : 1 PAIR EVERY 6 MONTHS"]
				x['heads']=['NAME','EMPLOYEE CODE','XS','S','M','L','XL','Total Qty','Remarks']
				x['item']=['name','ec','XS','S','M','L','XL','sum','']
		
		if x:
			return x
		return False

if __name__=="__main__":
	x=Report('safety_shoes')
	x.safety_shoes_stock_report()
