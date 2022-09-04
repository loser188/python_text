# 有一个元素序列，想知道序列中出现次数最多的元素
# collections模块中的Counter类正是为此设计的
from collections import Counter

words=[
    'aa','dad','asd','aa','sdsd','la','la',
]
word_counts=Counter(words)
top_three=word_counts.most_common(3)
print(top_three)

# counter 底层是一个字典，在元素和它们出现的次数之间做了映射
# counter 的另外一个特性就是可以同各种数学运算操作结合起来