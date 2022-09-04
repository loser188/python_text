# 序列中含有一些数据，我们需要提取出其中的值或根据某些标准对序列做删减
# 要筛选序列中的数据，通常最简单的方法是使用列表推导式
import math
from itertools import compress

mylist=[1,3,-4,2,4,5,7,2,2,-1]
print([n for n in mylist if n > 3])
# 使用列表推导式的一个潜在缺点是如果原始输入非常大的话，会产生一个庞大的结果，可以使用生成器表达式通过迭代的方式产生筛选的结果

pos=(n for n in mylist if n>3)
print(pos)
for x in pos:
    print(x)

# 有时候筛选的标准没法简单额地表示在列表推导式或生成器表达式中。可以将处理筛选逻辑的代码放到单独的函数中，然后使用内建的filter()函数处理。

values=['1','2','-3','f','4','n/a','s']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False

ivals=list(filter(is_int,values))
print(ivals)
# filter创建了一个迭代器，因此如果我们想要的式列表形式的结果，加上list
# 列表推导式和生成器表达式通常是用来筛选数据最简单和直接的方式。同时也具备对数据做转换的能力。

mylist=[1,2,4,3,5,7,3,-1,3,5,-4]
print([math.sqrt(n) for n in mylist if n > 0])

# 关于数据筛选，有一种情况是用新值替换掉不满足标准的值，而不是丢弃它们。
clip_neg=[n if n>0 else 0 for n in mylist]
print(clip_neg)

# itertools.compress（）,它接受一个可迭代对象以及一额布尔选择器作为输入。输出时
# 他会给出所有在相应的布尔选择器为True的可迭代对象元素。如果想把对一个序列的筛选结果施加到另一个相关的序列上时，这就会非常有用。
address=[
    '5412 n clark',
    '5148 n clark',
    '5800 E 58th',
    '2122 n clark',
    '5645 n ravenswood'
]
counts=[0,3,10,4,1,7,6,1]
# 现在我们想构建一个地址列表，其中相应的count值要大于5.
more5=[n>5 for n in counts]
print(more5)

print(list(compress(address, more5)))