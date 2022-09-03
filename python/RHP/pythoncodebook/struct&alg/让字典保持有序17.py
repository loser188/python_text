# 创建一个字典，同时对当前字典做迭代或序列化时，也能操作其中的元素

# 要控制字典中的元素的顺序，可以使用collection模块中的OrderedDict类，对字典做迭代时，会严格按照元素初始添加的顺序进行。
from collections import OrderedDict
import json

d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4

for key in d:
    print(key,d[key])

# 当想构建一个映射结构以便稍后对其做序列化或编码成另一种格式时，OrderedDict就显得特别有用。
print(json.dumps(d))

# 在OrderDict内部维护一个双向链表，会根据元素加入的顺序来排列键的位置。第一个新加入的元素放置在链表的末尾。接下来对已存在的键
# 赋新值不会改变键的位置
# OrderedDict的大小是普通字典的2倍。由于它额外创建的链表所致。

