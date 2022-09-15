# 想从序列中随机选出元素，或生成随机数
# random模块中有各种随机函数可以用于需要随机数和随机选择的场景
import random

values=[1,2,3,4,5,6,7]
print(random.choice(values))

# 随机删除元素
print(random.sample(values, 2))

#打乱顺序
print(random.shuffle(values))

#产生随机数
print(random.randint(0, 10)) #两个分数是随机边界

# 得到N个随机比特位所表示的整数
print(random.getrandbits(10))

# python random模块采用马特塞特旋转算法 也叫做梅森旋转算法，是一个确定性算法，可以通过random.seed()来修改初始的种子值
print(random.seed()) # 基于操作系统的时间
print(random.seed(12345))  # 限定种子
print(random.randint(1,10))

# random还具有计算均匀分布、高斯分布和其他概率分布的函数

# random.uniform()可计算均匀分布值
# random.gauss()计算正态分布

#random 不要用来生成密码随机数
