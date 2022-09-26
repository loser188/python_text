# 将二进制数据直接读取到一个可变缓冲区中，中间不经过任何拷贝环节，  我们想原地修改数据再将它写回到文件中

# 可以使用文件对象的readinto()方法
import os


def read_into_buffer(filename):
    buf=bytearray(os.path.getsize('mybannary.bin'))
    with open('myBannary.bin','rb') as f:
        f.readinto(buf)

