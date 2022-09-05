# 需要调用一个换算（reduction）函数（sum、min、max），但首先得对数据做转换或筛选
# 在函数参数中使用生成器表达式
nums=[1,2,3,4,5]
s=sum(x*x for x in nums)
print(s)
