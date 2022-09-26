# 已经编写好一个函数，但是希望参数附加上一些额外的信息
# 函数的参数注解
def add(x:int ,y:int)->int:
    return x+y


print(add(1, 5))

# 函数注解只会保存在函数的__annotions__属性中。
print(add.__annotations__)
