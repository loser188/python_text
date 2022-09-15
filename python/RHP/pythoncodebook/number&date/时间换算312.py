# 换算时间
# 使用detetime模块
from datetime import timedelta, datetime
import time
from dateutil.relativedelta import relativedelta

a=timedelta(days=2,hours=6)
b=timedelta(hours=4.5)
print(a+b)
c=a+b
print(c.days)
print(c.seconds)

# 表示特定日期，使用datetime实例并使用标准的数学运算来操作
a=datetime(2012,9,23)
print(a+timedelta(days=10))
b=datetime(2012,12,21)
d=b-a
print(d)

now=datetime.today()
print(now)

#date模块是可以正确处理闰年的

# dateutil的功能更强大

a=datetime(2012,9,23)
print(a + timedelta(days=3))


a+relativedelta(months=+1)

b=datetime(2012,12,21)
d=b-a
print(d)
