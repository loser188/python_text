#想要一个能够将键映射到多个值的字典

# 将这多个值保存到另一个容器或者列表的集合中
from collections import defaultdict

d={
    'a':[1,2,3],
    'b':[4,5]
}
#如果想保留元素插入的顺序就使用列表，消除重复元素，就用集合。

# 可以利用collectionsm模块中的defaultdict类。该类最大的一个特点就是会自动初始化第一个值，这样只关注添加元素即可

d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
print(d)

d=defaultdict(set)
d['a'].add(1)
d['a'].add(3)
d['a'].add(3)
print(d)

#需要注意的是，该类会自动创建字典表项以待稍后的访问（即使这些表项在当前字典中还未找到）。如果不想要该功能，在普通的字典上用setdefault()
d={}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(3)
d.setdefault('b',[]).append(4)
print(d)

#创建一键多值的字典很容易，但是初始化就很难