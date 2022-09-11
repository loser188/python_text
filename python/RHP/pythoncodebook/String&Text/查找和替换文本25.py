# 对字符串中的文本做查找和替换
# 使用str.replace即可
import re
from calendar import month_abbr

text='yeah,but no,but yeah,but no,but yeah'
text=text.replace('yeah','yep')
print(text)

# 针对更为复杂的模块，可以使用re模块的sub()函数/方法。
text='Today is 11/27/2012.pycon starts 3/13/2013.'
text=re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text) # 将符合第一种的正则替换为第二种正则
print(text)

# 对于更加复杂的情况，可以指定一个替换回调函数

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

def change_date(m):
    mon_name=month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
print(datepat.sub(change_date, text))
# 可以使用re.subn()
newtext,n=datepat.subn(r'\3-\1\2',text)
print(newtext,n)
