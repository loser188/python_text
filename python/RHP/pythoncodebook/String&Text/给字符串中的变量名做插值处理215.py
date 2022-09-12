# 字符串中嵌入的变量名称会以变量的字符串值形式替换掉
# python不支持在字符串中对变量做简单的值替换，可以通过formate方法模拟
import sys

s='{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# 如果要被替换的值确实能在变量中找到，可以将format_map()和vars()联合起来使用
name='Guido'
n=37
print(s.format_map(vars()))

# vars()的一个微妙的特性是它也能作用于类实例上
class Info:
    def __init__(self,name,n):
        self.name=name
        self.n=n
a=Info('Guido',37)
print(s.format_map(vars(a)))

# frame hack 技巧
# def sub(text):
#     return text.format_map(safesub(sys._getframe(1).f_locals))


