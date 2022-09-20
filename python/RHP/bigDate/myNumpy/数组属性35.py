# shape
# 语法  ndarray.shape
# 返回一个包含数组维度的元组，也可以用于调整数组大小
import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print(a.shape) # 返回  行    列

a=np.array([[1,2,3],[4,5,6]])
a.shape=(3,2)
print(a)

# 还可以使用reshape函数来调整数组大小
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(3,2)
print(b)


# ndim
# 语法： ndarray.ndim
# 返回数组的维数
a=np.arange(24)
print(a.ndim)
print(a)
# 调整大小
a=a.reshape(8,3)
print(a)
print(a.ndim)


# itemsize
# 语法： numpy.itemsize
# 返回数组中每一个元素的字节单位长度
print(a.itemsize)

# flags
# 语法： numpy.flags
# 返回当前值
print(a.flags)
# c_c 数组位于单一的、c风格的连续区段内
# f_c 数组位于单一的 fortran风格的连续区段内
# ow 数组的内从从其他对象处借用
# wr 数据区域可写入，将它设置为false会锁定数据，变为只读
# al 数据和元素都适当的对齐到硬件上
# up 数组的一个副本，这个数组释放时，原数组会由这个数组中的元素去更新

