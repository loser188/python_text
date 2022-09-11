# 想在字符串的开始、结尾或中间去掉不需要的额字符。
# strip()方法可以用来从字符串开始和结尾去掉字符,lstrip和rstrip可分别从左或从右侧开始去除字符串的操作。
import re

s=' hello Word\n'
print(s.strip()) # 默认除去空格符
print(s.lstrip())
t="-------hello======"
print(t.lstrip('-'))
print(t.strip("-=-")) #会将字符串解析为字符  然后去除所有的该字符串中的字符

#需要注意的是,strip并不会对文本中间的内容产生作用
s=' hello  world   \n'
print(s.strip())

# 如果要对里面的内容也产生作用，使用replace函数或正则表达式
print(s.replace(' ', ""))

print(re.sub('\s+', " ", s))

# 和迭代配合打开文件 完成生成器
# with open('rhp.text') as f:
#     lines=(line.strip()) for line in f)
#     for line in lines:
#         ''''''

