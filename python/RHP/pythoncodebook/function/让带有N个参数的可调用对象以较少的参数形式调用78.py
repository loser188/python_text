#  想要减少函数的参数数量
# 使用functools.partial()函数
import math
from functools import partial


def spam(a,b,c,d):
    print(a,b,c,d)


spam(1, 2, 3, 4)

# 使用partial()来对参数赋值
s1=partial(spam,1)
s1(2, 3, 4)
s2=partial(spam,d=42)
s2(1,2,3)


# 计算两点之间的距离
points=[(1,2),(3,4),(5,6),(7,8)]
def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)


print(distance(points[0], points[1]))
print(distance(points[2], points[3]))


