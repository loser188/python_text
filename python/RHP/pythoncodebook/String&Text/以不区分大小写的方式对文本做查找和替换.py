# 以不区分大小写的方式在文本中进行查找 替换
# 使用re模块并且对各种操作都要加上re.IGNORECASE的标记
import re

text='UPPER PYTHON,1lower python,mixed python'
print(re.findall('python', text, flags=re.IGNORECASE))

# 待替换的文本与匹配的文本大小写并不吻合
# 使用支撑函数修正这个问题
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.isllower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace()


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))