# Q 需要从可迭代对象中分解出N个元素，但是这个可迭代对象的长度可鞥超过N，会导致出现分解值过多的异常

# A python的“*表达式“可以用来解决这个问题

#假设开设了一门课程，并决定在期末的作用成绩中去掉第一个和最后一个，只对中间剩下的成绩做平均分统计。


grades={99,87,67,100,40,30,200}
def drop_first_last(grades):
    first,*middle,last = grades
    print(middle)#很奇怪，为什么没有按顺序来？
    return sum(middle)/len(middle)

print(drop_first_last(grades))

#另一个假设是有一些用户记录，记录由姓名和电子邮件地址组成，后面跟着任意数量的电话号码。
record={'dave','12312321@s.com','121212','0998889'}
name,emial,*photo_number=record
print(f"{name},{emial},{photo_number}")

#需要注意的是，*表达式不会做类型检查，也不会做判空，所以如果不加其他操作，*表达式的结果很可能无意义

#*号表达式在迭代一个变长的元组序列时尤其有用
records=[
    {'foo',1,2},
    {'bar','hello'},
    {'foo',3,4}
]

def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)

#在拆分splitting操作时，也非常有用
line='nobody:*:-2:-2:Unpasdad User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh=line.split(':')
print(f"{uname},{fields},{homedir},{sh}")

#有时候可能想分解出某些值然后丢弃它们。在分解的时候，不能只指定一个单独的*，但是可以使用几个常用的来表示丢弃的变量名
record={'acms',50,123.34,(12,18,2012)}
print(record)
name,*_,(*_,year)=record
print(name)
print(f"{name},{year}")

#需要注意的是，数据并不是按照输入时的存储的，具体要看打印出来的结果。
