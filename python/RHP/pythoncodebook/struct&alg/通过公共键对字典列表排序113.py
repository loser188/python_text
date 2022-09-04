# 有一个列表字典 根据一个或多个字典中的值来排序
# 利用operator模块中的itemgetter函数
from operator import itemgetter

rows=[
    {'fname':'aaa','lname':'bbb','uid':333},
    {'fname':'bbb','lname':'ccc','uid':222},
    {'fname':'ccc','lname':'ddd','uid':111},
]

rows_by_fname=sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)

rows_by_uid=sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)