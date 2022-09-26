# 希望函数只通过关键字的形式接受特定的参数  限制传参
def recv(maxsizee,*,block):
    print(maxsizee)
    print(block)

# recv(1024,True)
recv(102,block=True)

# 用来实现为可接受任意数量的位置参数的函数来指定关键字参数
def mininum(*valus,clip=None):
    m=min(valus)
    if clip is not  None:
        m=clip if clip>m else m
    return m


print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))

# def myf(*args,**kwargs):
#     print(args)
#     print(kwargs)
# myf(1,2,3,4,'asdasd',kwargs=[[1,2,1,2],['sdasdas']])