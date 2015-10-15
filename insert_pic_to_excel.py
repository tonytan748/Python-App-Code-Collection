#coding:utf-7
import os
import xlwt
from PIL import Image

path=os.path.dirname(__file__)

def test_image():
    w=xlwt.Workbook()
    ws=w.add_sheet('a test sheet')
    ws.write(0,2,"this is a data")

#    jpg_file=os.path.join(path,"a.jpg")
    convert()
    new_file=os.path.join(path,"a.bmp")
    if os.path.exists(new_file):
        print "exists"
#    a=Image.open(jpg_file)
#    a.save(new_file)
#    if os.path.exists(new_file):
#        new_file_1=Image.open(new_file)
#    new_file=a.convert("BMP")
    try:
        ws.insert_bitmap(new_file,2,3)
    except Exception as e:
        print e
    w.save("test.xls")

def convert():
    jpg_file=os.path.join(path,"a.jpg")
    new_file=os.path.join(path,"a.bmp")
    Image.open(jpg_file).save(new_file)

if __name__=="__main__":
    test_image()
