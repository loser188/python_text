# 想要迭代的元素包含在多个序列中，对这些序列同时遍历

# 使用zip函数来同时遍历多个序列
from itertools import zip_longest

xpts=[1,5,4,2,7]
ypts=[101,78,37,15,62,99]
for x ,y in zip(xpts,ypts):
    print(x,y)  # 从结果看 只会遍历相同的长度

# zip函数的原理是创建出一个迭代器，该迭代器产生出元组(x,y)，x来自A  y来自B
# 想要遍历长数组  使用itertools.zip_longest()来代替
for i in zip_longest(xpts,ypts):
    print(i)

# 使用zip快速构建字典
c=dict(zip(xpts,ypts))
print(c)

# zip只是创建了一个迭代器