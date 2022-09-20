# numpy数组创建例程

# numpy.empty
# 创建指定形状和dtype的未初始化数组
import numpy
import numpy as np
from numpy.core import shape

# numpy.empty(shape,dtype=float,order='C')

x=np.empty([3,2],dtype=int)
print(x)
# 数组元素未随机值


#numpy.zeros
# 返回特定大小，以0填充的新数组
# numpy.zeros(shape,dtype=float,orer='C')
x=np.zeros([3,4])
print(x)

# numpy.ones
# 返回特定大小，以1填充的新数组
#numpy.ones(shape,dtype=None,order='C')
x=np.ones([2,5])
print(x)


