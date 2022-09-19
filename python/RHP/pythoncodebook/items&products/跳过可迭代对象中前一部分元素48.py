# itertools模块可以跳过某些元素
# 该函数返回的迭代器会丢弃序列中的前面几个元素，只要它们在所提供的函数中返回Ture即可。
from itertools import dropwhile

with open("test_file") as f:
    for line in f:
        print(line,end="")

with open("test_file") as f:
    for line in dropwhile(lambda  line:line.startswith('python'),f):
        print(line,end='')