# 有一系列的字典或对象实例，根据某个特定的字段来分组迭代数据
# itertools.groupby()函数在对数据进行分组时特别有用。
from operator import itemgetter
from itertools import groupby

rows=[
    {'address':'54321 n clark','date':'07/01/2012'},
    {'address':'5418 n clark','date':'07/04/2012'},
    {'address':'5800 E 58th','date':'07/01/2012'},
    {'address':'2122 N clark','date':'07/03/2012'}
]

rows.sort(key=itemgetter('date'))

for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)

# groupby 创建了一个迭代器，而每次迭代时都会返回一个值（value)和一个子迭代器（sud_iterator),这个子迭代器可以产生所有在该分组内具有该值的项
# 这里首先要根据感兴趣的字段对数据进行排序，因为groupby只能检查连续的项。
