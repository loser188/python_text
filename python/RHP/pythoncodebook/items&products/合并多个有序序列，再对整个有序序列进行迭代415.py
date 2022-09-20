# 对一组有序序列合并再迭代
# 可以使用heapq.merge（）
import heapq

a=[1,4,7,7,10]
b=[2,5,6,11]
for c in heapq.merge(a,b):
       print(c)

# d对于提供的参数不会进行一次性读取
# 该函数只做简单的归并操作
