# 定义一个函数或方法，其中有一个或多个参数是可选的并带有默认值
def spam(a,b=42):
    print(a,b)
spam(1)
spam(3,10)

# 如果默认值是可变容器的话，None作为默认值
def spam(a,b=None):
    if b is None:
        b=[]


# 默认参数的函数，只有在定义的时候才绑定一次
