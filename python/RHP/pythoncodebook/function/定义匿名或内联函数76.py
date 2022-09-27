# 短小的函数   不希望使用def显示定义
# 可以通过lambda表达式来代替
add=lambda x,y:x+y
print(add(2, 3))
print(add('hello', 'world'))
names=['David Beazley','Brian Jones','Raymond Hettinger','Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
