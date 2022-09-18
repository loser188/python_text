#实现一个自定义的迭代模式，使其区别于内建函数
# 使用迭代生成函数

def frange(start,stop,increment):
    x=start
    while x<stop:
        yield x
        x+=increment

for n in frange(0,4,0.5):
    print(n)

#yield 函数会返回当前元素，并终止，但是，当再次运行时，会在yield之后的代码继续执行。
# yield语句会将其转变成一个生成器。生成器只会在响应迭代操作时才运行。