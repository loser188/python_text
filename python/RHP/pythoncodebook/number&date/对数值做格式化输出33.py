# 需要对数值做格式化输出，包括控制位数、对齐、
# 对单独的数做格式化输出，使用内建的format函数即可
x=1234.5678
print(format(x, '0.2f'))

print(format(x, '>10.1f'))

print(format(x, '<10.1f'))

#使用科学计数法

print(format(x, 'e'))