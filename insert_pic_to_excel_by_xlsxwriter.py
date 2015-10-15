#coding:utf-8
#use xlsxwriter is easy to insert pic to excel and donot mind the pic format.

import os
from xlsxwriter.workbook import Workbook

workbook=Workbook("a.xlsx")
worksheet=workbook.add_worksheet()
worksheet.write("B2","insert a image")
worksheet.insert_image("C4","a.jpg")
workbook.close()
