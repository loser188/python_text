#想在某个集合中找到最大或最小的N个元素
#heapq模块中有两个函数，nlargest()和nsmallest()
import heapq
from multiprocessing import heap

nums=[1,2,4,5,7,4,6,8,5,8,9,6,4,8,9,0]
print(heapq.nlargest(3,nums),"最大的")
print(heapq.nsmallest(3,nums),"最小的")

#这两个函数都可以接受一个参数Key,从而允许工作在更加复杂的数据结构上
portfolio=[
    {'name':'rhp','shares':100,'price':91.1},
    {'name':'rhp1','shares':99,'price':93.1},
    {'name':'rhp2','shares':98,'price':94.1},
    {'name':'rhp3','shares':97,'price':90.1},
    {'name':'rhp4','shares':96,'price':99.1},
    {'name':'rhp5','shares':95,'price':88.1},
    {'name':'rhp6','shares':0,'price':90.1},
]
chrsp=heapq.nsmallest(3,portfolio,key=lambda s:s['price'])

expensice=heapq.nlargest(3,portfolio,key=lambda s:s['price'])

print(f"{chrsp}")
print(f"{expensice}")

#如果正在寻找最大或者最小的N个元素，且同集合中元素的总数目相比，N很小。可以尝试以下函数
nums=[1,8,3,4,6,7,9,0,5,4,3,2,5,6,7,8]
heap=list(nums)
heapq.heapify(heap)
print(heap)

#堆最好的特性就是，0号为永远是最小的。此外，接下来的元素可以依次通过heap.heapify方法得到，且是Ologn复杂度

#当要找的元素数量相对较小时，nlargest和nsmallest才是最合适的。
#如果只是找最大或者最小的，min和max会更快。