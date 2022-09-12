#合并字符串
# 最快的是使用join函数
parts=['IS','Chicago','Not','Chicago?']
print(' '.join(parts))
# join操作其实是字符串对象的一个方法。这么设计的部分原因是因为想要合并在一起的对象可能来自各种不同的数据序列。
# 比如，在每一种数据结构时上都实现一边join函数，就太冗余了。

# 如果只是想简单的连接一些字符串，使用+号就可以了

# 针对更加复杂的字符串格式化操作，+操作同样可以作为format的代替。
a='Is Chicago'
b='Not Chicago?'

print('{} {}'.format(a,b))
print(a+" "+b)

# 如果想在源代码中将字符串面值合并在一起，可以简单的将它们排列在一起 不加+操作符
a='Hello' 'world'
print(a)

#'+'比join要慢许多，因为+=操作都会创建一个新的字符串对象。
# 最好的做法先收集所有要连接的部分，最后再一次将它们连接起来
# 利用生成器表达式在将数据
# 转换为字符串的同时完成连接操作
data=['ACME',50,91.1]
data=','.join(str(d) for d in data)
print(data)

# 一种高级的打印操作
c='c'
print(a,b,c,sep=':',end=']') #sep函数是设置分隔符   print在p3中作为函数，其中可接受sep和end 两个函数，一个是分隔符，一个是结尾标志


