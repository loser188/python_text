# 想对迭代器和生成器做切片处理，Itertools.islice()函数是完美的选择

def count(n):
    while True:
        yield n
        n+=1
c=count(0)
# print(c[10:20])
import itertools

for x in itertools.islice(c,10,20):
    print(x)