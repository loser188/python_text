# 读写csv文件中的数据
# 大部分的vsv数据都可以使用cvs库来解决
import csv

with open('mycvs01.csv') as f:
     f_cvs=csv.reader(f)
     headers=next(f_cvs)
     for row in f_cvs:
         print(row)
     