# Numpy中定义的最重要的对象是称为ndarray的N维数组类型，描述相同类型的元素集合，可以使用基于0的索引访问集合中的项目
# ndarray中每个元素使用相同大小的块，每个元素是数据类型对象的对象（dtype)
import numpy as np

# numpy.array(object,dtype=None,copy=True,order=None,s=0)
# object:任何暴露数组接口方法的对象都会返回一个数组或任何嵌套
# dtype：数组所需的数据类型，可选
# copy: 可选：默认为ture,对象是否被复制
# order: C按行，F按列，A默认
# subok: 默认返回的数组强制为基类数组，如果为true，就返回子类
# ndmin:指定返回数组的最小维数

a=np.array([1,2,3])
print(a)

# 多余一个维度
a=np.array([[1,2],[3,4]])
b=[]
b.append([[1,2],[3,4]])
print(a)
print(b)

# 最小维度
a=np.array([1,2,3,4,5],ndmin=2)
print(a)

# dtype参数
a=np.array([1,2,3],dtype=complex)
print(a)

# ndarray对象由计算机内存中一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案
