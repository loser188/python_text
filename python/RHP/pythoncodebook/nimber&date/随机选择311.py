# 想从序列中随机选出元素，或生成随机数
# random模块中有各种随机函数可以用于需要随机数和随机选择的场景
import random

values=[1,2,3,4,5,6,7]
print(random.choice(values))

# 随机删除元素
print(random.sample(values, 2))

#打乱顺序
print(random.shuffle(values))