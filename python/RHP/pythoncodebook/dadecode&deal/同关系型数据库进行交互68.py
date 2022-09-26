# 选择、插入、删除关系型数据库中的数据
# 在python中，表达行数据的标准方式是采用元组序列
import sqlite3

stocks=[
    ('GOOG',100,490.1),
    ('aaple',50,545.75),
    ('FB',150,7.45),
    ('HPQ',75,33.2)
]

db=sqlite3.connect('databases.db')
