# 代码是通过位置（索引、下标）来访问列表或元组的，但有时候会使代码变得难以阅读，想通过名称来访问元素。

# collections.namedtuple（）命名元组只增加了极小的开销就提供了这些便利
# 实际山collections.namedtuple是一个工厂方法，它返回的是python中标准元组类型的子类。我们提供给它一个类型的名称以及相应的字段，它就返回一个可实例化的类
# 并且定义好字段传入值
from collections import namedtuple

Subsriber=namedtuple('Subscriber',['addr','joined'])
sub=Subsriber('joneS@example.com','2012-10-19')
print(sub)
