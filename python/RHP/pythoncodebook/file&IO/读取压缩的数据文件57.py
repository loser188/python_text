# 读取gzip或bz2格式的压缩文件

# 类似原来的open操作
import gzip

with gzip.open('myzip.zip','rt') as f:
    text=f.read()
    print(text)

with gzip.open('myzip.zip','wt') as f:
    f.write('asdasdasd')

# 如果没有指定模式  默认就是二进制

# 写入文件时 压缩文件可以通过compresslevel关键参数来指定
with gzip.open('myzip.zip','wt',compresslevel=5) as f:
    f.write('////////')

# 默认级别是9  最高级别

# 压缩文件打开  zgip和bz2可以能够对已经以二进制模式打开的文件进行叠加操作

f=open('myzip.zip','rb')
with gzip.open(f,'rt') as g:
    text=g.read()
    print(text,'llllllll')