# 有两个字典，我们想在它们中间找到可能相同的地方（相同的键、相同的值等）
a={
    'x':1,
    'y':2,
    'z':3
}

b={
    'w':10,
    'x':11,
    'y':2
}

# 想找出这两个字典中的相同之处，只需通过keys或者items()方法执行常见的集合操作

# 相同的键
print(a.keys() & b.keys())

# a独有的键
print(a.keys() - b.keys())

# 有相同的键和值的
print(a.items() & b.items())

# 创建一个新的字典，其中会去掉某些键
c={key:a[key] for key in a.keys()-{'z','w'}}
print(c)

