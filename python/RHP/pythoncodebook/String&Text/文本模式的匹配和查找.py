# 按照特定的文本进行匹配或查找
# 如果只是匹配简单的文案，str.find()\str.endwith()\str.startwith()之类的函数就可解决
import re

text='yeah,but no,but yeah,but no,but yeah'
print(text=='yeah') # quan匹配
print(text.startswith('yeah')) # 匹配开头
print(text.endswith('no')) #匹配结尾
print(text.find('no')) # 默认返回匹配到的第一个

# 更为复杂的需要使用正则表达式以及re模块。
text1='11/27/2012'
text2='nov 27,2012'
if re.match(r'\d+/\d+/\d+',text1): # 正则表达
    print("yes")
else:
    print("no")

# 如果打算针对同一种模式做多次匹配，那么通常会将正则表达式模式编译成一个模式对象
datepat=re.compile(f'\d+/\d+/\d+')
if datepat.match(text1):
    print("yes")
else:
    print('no')
    # match()方法总是尝试在字符串的开头找到匹配项，如果想找出所有的匹配项，就应该使用findall方法
text='Today is 11/27/2012,pycon strarts 3/13/2013'
print(datepat.findall(text))

# 当定义正则表达式时，我们将会将部分模式使用括号包起来的方式引入捕获组。
datepat=re.compile(f'(\d+)/(\d+)/(\d+)')
# 捕获组通常能够简化后续对匹配文本的处理，因为每个组的内容都可以单独提取出来。
m=datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

text='Today is 11/27/2012,pycon starts 3/13/2013.'
print(datepat.findall(text))
for month,day,year in datepat.findall(text):
    print('{}-{}-{}'.format(year,month,day))
# findall搜索整个文本并找出所有的匹配项然后将它们以列表的形式返回。如果想以迭代的方式找出匹配项，可以使用finditer()方法
for m in datepat.finditer(text):
    print(m.groups())

# match方法只会检查字符串的开头。有可能出现匹配的结果并不是想要的结果
m=datepat.match('11/27/2012abcdef')
print(m)
print(m.groups())
# 如果想要精确匹配，确保模式中包含一个结束标记（$）
datepat=re.compile(r'(\d+)/(\d+)/(\d+)$')
m=datepat.match('11/27/2012abcdef') # 该匹配不成功，2012abcd不是纯数字
# print(m.group(),'全匹配，分组')
m=datepat.match('11/27/2012')
print(m.groups(),'精确匹配')

# 只想执行简单的文本匹配和搜索操作，通常可以省略编译步骤，直接使用re模块中的函数
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
# 模块级的函数会对最近编译过的模式做缓存处理，因此打算多次执行匹配操作/查找的话，通常需要将模式编译后再重复使用









