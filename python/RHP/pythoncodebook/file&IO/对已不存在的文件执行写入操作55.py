# 对文件执行写入操作，只有当该文件不存在时才成功
#  可以通过open()函数中 X  和 W模式来解决。

with open("myFile.txt",'wt') as f:
    f.write('hello\n')

with open('myFile.txt','xt') as f:
    f.write('Hello\n') # 会报该文件以存在

    # 对于二进制文件  xb可以替代xt
