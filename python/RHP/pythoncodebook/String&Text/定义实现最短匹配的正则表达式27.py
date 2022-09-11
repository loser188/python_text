# 找出最短的额模式匹配  正则表达式
# 这个问题通常会在匹配的文本被一对开始和结束分隔符包起来的时候出现
import re

str_pat=re.compile(r'\"(.*)\"')
text1='Computer says"no."'
print(str_pat.findall(text1))
text2='Computer says "no. Phone says "yes."'
print(str_pat.findall(text2))


