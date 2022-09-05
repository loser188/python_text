# 需要将字符串拆分为不同的字段，但是分割符在整个字符串中并不一致
# split()方法只能处理非常简单的情况，且不支持多个分隔符，对分隔符周围可能存在额地空格也无能为力。使用re.split
import re

line='asdf fjdk;afed,asdf,    foo'
print(re.split(r'[;,\s]\s*', line))