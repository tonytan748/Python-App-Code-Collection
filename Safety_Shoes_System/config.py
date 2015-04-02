#coding:utf-8
import os,sys
import data

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
DATAFILE=os.path.join(FILEPATH,'system.db')
STATUS=os.path.join(FILEPATH,'status.txt')
TYPE=os.path.join(FILEPATH,'type.txt')
USER=os.path.join(FILEPATH,'user.txt')

GET_STATUS=data.get_items(STATUS)
GET_TYPE=data.get_items(TYPE)
GET_USER=data.get_items(USER)
GET_NAMES=data.get_name_list()