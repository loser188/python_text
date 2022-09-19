# 想迭代序列，但又想知道当前元素的索引

# 内建的enumerate()函数
my_list=['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)

# 可以传入起始位置，进行规范打印
for idx,val in enumerate(my_list,1):
    print(idx,val)