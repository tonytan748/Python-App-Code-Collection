#coding:utf-8
import os,sys
import data

SAFETY_SHOES=['issue_status','issue_from','issue_to','issue_date','issue_type','issue_size','issue_qty','issue_product','remarks','create_by','create_date']

GET_ITEMS=data.get_data('safety_shoes',SAFETY_SHOES)

GET_PRODUCT=data.get_product_name()
