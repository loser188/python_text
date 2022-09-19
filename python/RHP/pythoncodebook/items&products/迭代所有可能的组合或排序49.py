# 对一系列元素所有可能的组合或排列进行迭代
# itertools.permutations() 接受一个元素集合，将其中所有的元素重排序为所有的可能，并以元组序列的形式返回。
from itertools import permutations, combinations, combinations_with_replacement

items=['a','b','c']
for p in permutations(items):
    print(p)

for c in combinations(items,3):
    print(c)

#itertools.combinations_with_replacement()允许同一个元素多次出现
for c in combinations_with_replacement(items,3):
    print(c)