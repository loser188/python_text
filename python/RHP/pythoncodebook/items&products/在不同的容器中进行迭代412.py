# 解决多容器 同目标的循环问题
# itertools.chain()方法可以用来简化该任务，它接受一些列可迭代对象作为输入并返回一个迭代器，这个迭代器能够有效地掩饰一个事实————是在对多个容器进行遍历
from itertools import chain

a=[1,2,3,4]
b=['x','y','c',1,3]
c={1:2,4:'adasd','a':a}
for x in chain(a,b,c.values()):
    print(x) # 从结果看  不存在去重操作
# chain()不要求是同类型 但从结果看 对于字典 默认遍历key


