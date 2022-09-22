# 不要按行迭代  而是一系列固定大小的记录或数据
from functools import partial

RECORD_SIZE=32
with open('myFile.txt','rb') as f:
    records=iter(partial(f.read,RECORD_SIZE),b'')
    for r in records:
        print(r)