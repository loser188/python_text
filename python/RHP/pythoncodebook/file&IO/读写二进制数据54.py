# 读写二进制文件  图像、声音等
# 使用open（）函数的rb或者wb模块
with open('myBannary.bin') as f:
    date=f.read()
    print(date)

with open('myBannary.bin','wb') as f:
    f.write(b'Hello World')