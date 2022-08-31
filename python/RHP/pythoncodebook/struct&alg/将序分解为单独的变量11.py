# Q 将n给元素的元组或者序列分解为n个单独的变量

# A 任何序列或者可以迭代的对象，都可以通过一个简单的赋值操作来分解为单独的变量。唯一的要求是变量的总数和数据结构要与序列吻合
p=(4,5)
x,y=p
print(x,y)

data=['acme',50,91.1,(2012,12,21)]
name,shares,price,date=data
print(f"{name},{shares},{price},{date}")


# 不仅仅是元组或者列表，只要对象是可以迭代的额，就可以进行分解操作 包括字符串、文件、迭代器和生成器
s='hello'
a,b,c,d,e=s
print(f"{a},{b},{c},{d},{e}")

# 当我们要丢弃某些特定的值时，可以使用一个用不到的变量名来存储他

data=['acms',50,90.1,{2012,12,21}]
_,shares,price,_=data
print(f"{shares}, {price}")