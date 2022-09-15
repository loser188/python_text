# 对小数进行精确计算
from decimal import Decimal, localcontext

a=4.2
b=2.1
print(a+b)
print(6.3==a+b)

# 底层cpu和IEEE浮点算数计算标准的一种‘特性’
# 想实现高精度的计算，可以使用decimal模块
a=Decimal('4.2')
b=Decimal('2.1')
print(a + b)
print(a + b == Decimal('6.3'))

# 要做到控制精度，四舍五入等，需要构建一个上下文环境
with localcontext( ) as ctx:
    ctx.prec=3
    print(a/b)
print(a/b)

#decimal实现了IBM的通用十进制算数规范
# float提供17位的精度