# 对大型的数组或者网格进行计算
# 对任何涉及数组的计算密集型任务，使用numpy numpy的主要特性是为python提供数组对象。
import numpy as np

x=[1,2,3,4]
y=[5,6,7,8]
# print(x*2)
# print(x+10)
#
# print(x+y)

ax=np.array(x)
bx=np.array(y)
print(ax*2)
print(ax+10)
print(ax*bx) #对位相乘


# numpy通过了一些”通用函数“的集合
print(np.sqrt(ax))

# 在底层 numpy数组的内存分配和C一样，是大块的连续内存，由同一种类型的数据组成。
grid=np.zeros(shape=(10000,10000),dtype=float)
print(grid)
#常用操作仍然可以同时施加在所有元素上
grid+=10
print(grid)
print(np.sin(grid))

# numpy 扩展了python列表的索引功能

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,1,12]])
print(a)
print(a[1]) # 第一行
print(a[:,1]) # 第一列
print(a[1:3,1:3]) #
print(a[1:3,1:3]+10)

a+=[100,101,102,103]
print(a)

print(np.where(a < 10, a, 10))