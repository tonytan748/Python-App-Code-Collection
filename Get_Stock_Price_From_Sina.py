#coding:utf-8
"""
Created on Wed Sep 16 09:02:48 2015
This one is get stock current price from sina stock
Return: save a txt file name is Table.txt

Due to use python2.7 and in the Pool.map(func,*args), the func must outside of class, so i have to create a function named "get_stock_price"

and in python 3.* this function just create in class.
@author: Administrator
"""

import os
import urllib2
import csv
import time

from multiprocessing.dummy import Pool

THREAD=10

def get_stock_price(stname):
    """Get stock price by stock number for once
    return a list include stock price and stock number"""
    x=[]
    this_url="http://hq.sinajs.cn/list={}".format(stname)
    datas=urllib2.urlopen(this_url)
    s=(datas.read()).split(',')
    if len(s)>3:
        present_price=s[3]
        status="-"
        if float(present_price)==0.0:
            present_price=s[2]
            status="TingPai"
        x.append(str(stname[2:]))
        x.append(present_price)
        x.append(status)
        return tuple(x)

def read_txt(stock_list_file):
    """read stock number list in a txt file
    return a list include all stock numbers"""
    lists=[]
    with open(stock_list_file) as f:
        for i in f.readlines():
            name=None
            x=(i.strip()).split(',')
            xx=x[0][-6:] if len(x[0])>6 else x[0]
            if len(xx)==6 and xx.startswith('6'):
                name="sh"+xx
            elif len(xx)==6 and not xx.startswith('6'):
                name="sz"+xx
            else:
                return
            if name:
                name="http://hq.sinajs.cn/list={}".format(name)
            lists.append(name)
        return lists

class StockList(object):
    """handler the stock list and get a stock price use multiprocessing.Pool.map
    return a list of stock list include number and price"""
    def __init__(self,func,stock_list,new_csv):
        self.f=func
        self.stock_list=stock_list
        self.new_csv=new_csv

    def get_stocks(self):
        global THREAD
        print len(self.stock_list)
        try:
            pool=Pool(THREAD)
            sdatas=pool.map(self.f,self.stock_list)
            pool.close()
            pool.join()
        except Exception as e:
            print e
            
        s=['\t'.join(i)+"\n" for i in sdatas if i]
#        print s
#      save to csv file.
#        with open(self.new_csv,'w') as f:
#            writer=csv.writer(f)
#            writer.writerow(['Stock Number','Price','Status'])
#            writer.writerows(s)
#            print "write success"
           
        with open(self.new_csv,'w') as f:
            f.writelines(s)
                    

def main(stock_lists):
    """set stock number file path&name and set output file name
    called the StockList class
    return save a txt file under the same path"""
    print "main start..."
    this_p=os.path.join(os.getcwd(),"Desktop")
    this_path=os.path.join(os.getcwd(),"StockList.txt")        
    o_data=os.path.join(os.getcwd(),'Table.txt')
    x=StockList(func=get_stock_price,stock_list=stock_lists,new_csv=o_data)
    x.get_stocks()
    print "end"
    
def doit():
    """loop refresh newest data and save it"""
    this_path=os.path.join(os.getcwd(),"StockList.txt")  
    print "System Running... ..."
    stock_lists=read_txt(this_path)
    while True:
        try:
            main(stock_lists)
        except Exception as e:
            print e
            pass
        time.sleep(3)

#doit()
if __name__=='__main__':
    doit()
