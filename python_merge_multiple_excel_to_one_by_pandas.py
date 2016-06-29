#coding:utf-8
import pandas as pd
from multiprocessing import Pool
import os
import glob


def get_file_list():
    file_path = os.getcwd()
    for item in glob.iglob('*.xls'):
        file_name = os.path.join(file_path,item)
        yield file_name

def get_data(table):
    print table
    with pd.ExcelFile(table) as xls:
        data = pd.read_excel(xls,xls.sheet_names[0],na_values=[''])
        return data

def main():
    pool = Pool(4)
    result = pool.map(get_data, get_file_list())
    pool.close()
    pool.join()

    for i in result:
        if os.path.exists(os.path.join(os.getcwd(),'web_safety_assets.csv')):
            print "add data ......."
            i.to_csv('web_safety_assets.csv',header=False,mode='a',encoding="utf-8")
        else:
            print "create table"
            i.to_csv('web_safety_assets.csv',encoding="utf-8")

if __name__=='__main__':
    main()
