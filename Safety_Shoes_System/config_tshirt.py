#coding:utf-8
import os,sys
import data

FILEPATH=os.path.join(os.path.split(sys.argv[0])[0],'data')
TSHIRT=['issue_status','issue_from','issue_to','issue_date','issue_type','issue_size','issue_qty','issue_color','issue_sex','issue_sleeve','issue_pocket','remarks','create_by','create_date']

COLOR=os.path.join(FILEPATH,'color.txt')
SIZE=os.path.join(FILEPATH,'size.txt')


GET_ITEMS=data.get_data('tshirt',TSHIRT)
GET_COLOR=data.get_items(COLOR)
GET_SIZE=data.get_items(SIZE)