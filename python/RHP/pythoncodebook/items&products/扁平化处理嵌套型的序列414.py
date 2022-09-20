# 有一个嵌套型的数据，想将它扁平化处理为一列单独数据
# 可以通过一个简单的带有 yeild form 解决
from collections import Iterable


def flatten(items,iqnore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,iqnore_types):
            yield from  flatten(x)
        else:
            yield x
items=[1,2,3,4,5,['a','d',{'?':'....'}]]
for x in flatten(items):
    print(x)

