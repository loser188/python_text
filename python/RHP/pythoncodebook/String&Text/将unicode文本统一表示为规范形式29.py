# 确保所有的字符都拥有相同的底层表示
# Unicode中，有些特定的字符可以被表示成多种合法的代码序列。
s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
print(s1)
print(s2)
