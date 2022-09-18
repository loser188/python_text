# 反向迭代序列中的元素
# 使用内建函数 reversed()函数
a=[1,2,3,4]
for x in reversed(a):
    print(x)

# 反向迭代只有在待处理的对象拥有可确定的大小或者对象实现了_reversed_()
# 如果都不满足 就转换位列表

f=open('test_file')
for line in reversed(list(f)):
    print(line,end='')

# 对象的类型转换时很耗费时间的

# 自定义实现反向迭代

class Countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        n=self.start
        while n>0:
            yield  n
            n-=1
    def __reversed__(self):
        n=1
        while n<=self.start:
            yield n
            n+=1


