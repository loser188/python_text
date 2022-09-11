# 清理掉文本中某些内容
# str。translate()方法

s='pyth^on\fis\towesome\r\n'
print(s)

#建立一个小型转换表
remap={
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None  #相当于删除
}
a=s.translate(remap)
print(a)

