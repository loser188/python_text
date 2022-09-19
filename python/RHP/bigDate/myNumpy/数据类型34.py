# NumPy数据类型
# numpy支持比python更多的数据类型
# bool=存储1字节的布尔值
# int=默认为整数，相当于C的long,通常为int32或int64
# intc=相当于C的int，通常为int32或int64
# intp=用于索引的整数，相当于C的size_t,通常为int32或int64
# int8=字节（-128~127）
#int16 16位整数（-32768~32767）
#int32 32位整数（-21亿~21亿）
#int64 64位整数（-9.。。~9.。。）
#。。

# numpy数值类型是dtype对象的实例，每个对象具有唯一的特性

# 数据类型对象描述了对应于数组的固定内存块的解释，取决于5个方面
# 1.数据类型（整数、浮点数或python对象）
# 2.数据大小
# 3.字节序（大端/小端）
# 4 在结构化类型的情况下，字段的名称、每个字段的数据类和占用内存大小
# 5 数据类型是子序列的性状和数据类型

# 字节顺序取决于数据类型的前缀  ”<"是小端  ”》“是大端

# dtype 语法构造 numpy.dtype(object,align,copy)
# object ：被转换为数据类型的对象
# align: 如果位ture，就向字段添加间隔，类似C结构
# copy: 生成dtype对象的新副本，如果为false，就是内建数据类型对象的引用

# 使用数组标量类型
import numpy as np

dt=np.dtype(np.int32)
print(dt)

dt=np.dtype([('age',np.int8)])
a=np.array([(10,),(20,),(30,)],dtype=dt)
print(dt)
print(a)

# 每个内建类型都有一个唯一定义符号
# b 布尔
# i 符号整数
# u  无符号整数
# f 浮点数
# c 复数浮点数
# m 时间间隔
# o python对象
# s,a  字节串
# u unicode
# v 原始数据 (void)