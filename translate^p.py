# coding: utf-8
import csv

with open('before.csv','r') as f:
    reader=csv.reader(f)
    fo=open('after.txt','w+')
    for i in reader:
        fo.write(i[0]+',')
    fo.close()
print('---------------------------------完成------------------------------')