#-*-coding:utf-8-*-
#This program is use in get the site laber costing basic in label costing data.

import os
import sys
import datetime

from collections import Counter

MESSAGE='''
Please input the project code.
If you want get all this project, you just input the first 5 number('14879'), 
Otherwise you must input full code ('12907 T' or '14854 H - 04')
Press 1 to exit system.
'''

thisfilepath=sys.argv[0]
filepath=os.path.dirname(thisfilepath)
filename=os.path.join(filepath,"manpower_summary.txt")

def check_report_and_return_list(filename,project_code):
	have_report=False
	with open(filename,'r') as f:
		cont=f.readlines()
	cout_t=(x.replace('\n','').replace('\r','') for x in cont)
	m=(x for x in cont_t if (x.split(','))[4].startswith(project_code))
	if m:
		have_report=True
	return (have_report,m)

def get_total_report(m)
	if m:
		for i in m:
			info={}
			info['name']=i[1]
			info['date']=i[38]
			info['working_time']=i[24]
			country=(i[2][0]).upper()
			if country=="B":
				info['country']="B"
			elif country=="I":
				info['country']="I"
			elif country=="C" or country=="P":
				info['country']="C"
			else:
				info['country']="N"
			if i[25]=="#N/A":
				info['t_salary']=0.0
			else:	
				info['t_salary']=float(i[25])

			if i[41]:
				info['accomodation']=float(i[41])
			else:
				info['accomodation']=0.0
			if i[42]:
				info['transportation']=float(i[42])
			else:
				info['transportation']=0.0
			if i[43]:
				info['levy']=float(i[43])
			else:
				info['levy']=0.0
			if i['date']:
				info['week_num']=count_weekday(i['date'])
			else:
				info['week_num']='0'
			yield info
			





def have_report(filename,project_code):
	print filename
	print project_code

	with open(filename,"r") as f:
		i=f.readlines()
		i=i.replace('\n').replace('')
#		a=i[0].split('\r')

	m=((x.split(','))[4] for x in i)
	mm= [(x.split(',')) for x in i if (x.split(','))[4].startswith(project_code)]
	print len(mm)
	cc=[[j.replace('\n','').replace('\r','') for j in i] for i in mm]
	print len(cc)

	aa=[]
	for i in mm:
		bb=[]
		for j in i:
			bb.append(j.replace('\n',''))
	aa.append(bb)
	print len(aa)
	j=0
	for ss in m:
		if str(ss).startswith(project_code):
			j=j+1
			print ss
			break
	if j==0:
		return False
	else:
		return True

def get_pro_report(filename,project_code):
	t_info=[]
	with open(filename,"r") as f:
		i=f.readlines()
#		a=i[0].split('\r')
	m=((x.split(',')) for x in i)
	for ss in m:
		if str(ss[4]).startswith(project_code):
			info={}
			info['name']=(ss[1]).upper()
			info['date']=ss[38]
			info['working_time']=ss[24]

			country=(ss[2][0]).upper()
			if country=="B":
				info['country']="B"
			elif country=="I":
				info['country']="I"
			elif country=="C" or country=="P":
				info['country']="C"
			else:
				info['country']="N"
			if ss[25]=="#N/A":
				info['t_salary']="0"
			else:	
				info['t_salary']=ss[25]

			if ss[41]:
				info['accomodation']=float(ss[41])
			else:
				info['accomodation']=0.0
			if ss[42]:
				info['transportation']=float(ss[42])
			else:
				info['transportation']=0.0
			if ss[43]:
				info['levy']=float(ss[43])
			else:
				info['levy']=0.0
			t_info.append(info)
	return t_info

def count_weekday(date_str):
	if date_str:
		d=date_str.strip()
		dat=datetime.date(int(d[:4]),int(d[4:6]),int(d[-2:]))
		x=datetime.date.isocalendar(dat)
		year=str(x[0])
		week=str(x[1])
		if len(week)==1:
			week="0"+week
		info=year+week
		firstday=getfirstday(info)
		lastday=firstday+datetime.timedelta(days=7)
		info=info+","+datetime.date.strftime(firstday,"%Y%m%d")+","+datetime.date.strftime(lastday,"%Y%m%d")
		return info

def return_pro_list(pro_list):
	a_list=[]
	for i in pro_list:
		week_n=str(i['week_num'])
		if a_list:
			for j in a_list:
				a={}
				if week_n == j['week_n']:
					j['week_n']=str(float(j.get(week_n))+float(week_n))
					j['salary']=str(float(j.get(salary))+float(i['t_salary']))
					j['accomodation']=str(float(j.get(accomodation))+float(i['accomodation']))
					j['transportation']=str(float(j.get(transportation))+float(i['transportation']))
					j['levy']=str(float(j.get(levy))+float(i['levy']))
				else:
					a['week_n']=str(float(week_n))
					a['salary']=str(float(i['t_salary']))
					a['accomodation']=str(float(i['accomodation']))
					a['transportation']=str(float(i['transportation']))
					a['levy']=str(float(i['levy']))
					a_list.append(a)
		else:
			a={}
			a['week_n']=str(float(week_n))
			a['salary']=str(float(i['t_salary']))
			a['accomodation']=str(float(i['accomodation']))
			a['transportation']=str(float(i['transportation']))
			a['levy']=str(float(i['levy']))
			a_list.append(a)
	return a_list

def get_list_by_day(pro_list):
	a_list=[]
	for i in pro_list:
		date=str(i['date'])
		if a_list:
			print len(a_list)
			for j in a_list:
				a={}
				if date==j['date']:
					j['date']=str(float(j.get(date))+float(date))
					j['salary']=str(float(j.get(salary))+float(i['t_salary']))
					j['accomodation']=str(float(j.get(accomodation))+float(i['accomodation']))
					j['transportation']=str(float(j.get(transportation))+float(i['transportation']))
					j['levy']=str(float(j.get(levy))+float(i['levy']))
				else:
					a['date']=str(float(date))
					a['salary']=str(float(i['t_salary']))
					a['accomodation']=str(float(i['accomodation']))
					a['transportation']=str(float(i['transportation']))
					a['levy']=str(float(i['levy']))
					a_list.append(a)
		else:
			a={}
			a['date']=str(float(date))
			a['salary']=str(float(i['t_salary']))
			a['accomodation']=str(float(i['accomodation']))
			a['transportation']=str(float(i['transportation']))
			a['levy']=str(float(i['levy']))
			a_list.append(a)
	return a_list

#Get country worker numbers
def get_worker_country_number(pro_list):
	a={}
	x=((i['name'],i['country']) for i in pro_list)
	y=Counter([i[1] for i in set(x)])
	if y["B"]:
		a['B']=y['B']
	else:
		a['B']=0
	if y["I"]:
		a['I']=y['I']
	else:
		a['I']=0
	if y["C"]:
		a['C']=y['C']
	else:
		a['C']=0
	return a

def getfirstday(weekflag):
	yearnum = weekflag[0:4]   #取到年份
	weeknum = weekflag[4:6]   #取到周
	stryearstart = yearnum +'0101'   #当年第一天
	yearstart = datetime.datetime.strptime(stryearstart,'%Y%m%d') #格式化为日期格式
	yearstartcalendarmsg = yearstart.isocalendar()  #当年第一天的周信息
	yearstartweek = yearstartcalendarmsg[1]  
	yearstartweekday = yearstartcalendarmsg[2]
	yearstartyear = yearstartcalendarmsg[0]
	if yearstartyear < int (yearnum):
		daydelat = (8-int(yearstartweekday))+(int(weeknum)-1)*7
	else :
		daydelat = (8-int(yearstartweekday))+(int(weeknum)-2)*7
	a = (yearstart+datetime.timedelta(days=daydelat)).date()
	return a

#sort project list and return 
def sort_data(p_dict,start_num=6):
	dict=sorted(p_dict.iteritems(),key=lambda d:d[0][start_num],reverse=False)
	return dict



def getreport(project_code):
	pro_list=get_pro_report(filename,project_code)

	day_summary=get_list_by_day(pro_list)
#	day_summary=sort_data(day_summary)

	worker_num=get_worker_country_number(pro_list)

	for i in pro_list:
		i['week_num']=count_weekday(i['date'])

	week_summary=return_pro_list(pro_list)

	date_t=datetime.datetime.strftime(datetime.date.today(),"%Y%m%d")
	save_file=str(date_t)+"_"+project_code+".csv"
	file_path=os.path.join(filepath,"Project_Label_Cosing")
	save_file_path=os.path.join(file_path,save_file)



	print "=========================="
	with open(save_file_path,"w") as f:
		print "Project Code,%s\n"%project_code
		print "Week Number,Start Day,End Day,Label Costing\n"

		f.write("Project Code,%s"%project_code)
		f.write("\n-----------------------------------\n")
		f.write("Week Number,Start Day,End Day,Label Costing\n")
		m=0.00

		for i in week_summary:
			print "%s\t%s\t%s\t%s\t%s"%(i['week_n'],i['salary'],i['accomodation'],i['transportation'],i['levy'])
			f.write("%s,%s,%s,%s,%s\n"%(i['week_n'],i['salary'],i['accomodation'],i['transportation'],i['levy']))
			m+=float(i['salary'])
		f.write('\n')
		f.write('TOTAL,%s\n'%str(m))

		print "\n"
		print "TOTAL,%s"%str(m)
		print "\n==================================\n"
		worker_print='''
Bengal Worker, %s\n
Indian Worker, %s\n
Chinese Worker, %s\n
TOTAL Worker, %s\n
		''' % (str(worker_num['B']),str(worker_num['I']),str(worker_num['C']),str(int(worker_num['B'])+int(worker_num['I'])+int(worker_num['C'])))
		print worker_print
		f.write(worker_print)

		f.write("\n==================================\n")
		f.write("Project Code,%s"%project_code)
		f.write("\n-----------------------------------\n")
		f.write("DATE,SALARY\n")

		for i in day_summary:
			f.write("%s,%s,%s,%s,%s\n"%(i['date'],i['salary'],i['accomodation'],i['transportation'],i['levy']))


def main():
	if os.path.exists(filename):

		while True:
			print  MESSAGE
			p=raw_input()
			project_code=p.strip()

			if project_code=="1":
				exit(1)
			elif len(project_code)<5:
				print "###The project code length is short.\n###Please check the project code and try again!"
				continue

			h_report=have_report(filename,project_code)
			if h_report is False:
				print "Cannot find this project report, please try again!"
				continue

			getreport(project_code)

	else:
		print "Cannot find the data file, you need inform administrator to resolve it."

main()
