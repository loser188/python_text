# 想从函数中返回多个值
# 返回一个元组
def myfun():
    return 1,2,3
a,b,c=myfun()
print(a)

# 尽管看起来返回了多个值，但实际上它只创建了一个元组而已
