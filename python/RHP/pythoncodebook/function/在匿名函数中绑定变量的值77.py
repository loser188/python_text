x=10
a=lambda y:x+y
print(a(x))
x=20
b=lambda y:x+y
print(b(x))

# 绑定特定的值  不改变

x=10
a=lambda y,x=x:x+y
print(a(10))