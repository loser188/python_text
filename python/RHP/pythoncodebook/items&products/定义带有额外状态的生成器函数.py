# 定义一个生成器函数，但是它有一些其他状态
# 如果想让生成器状态暴露给用户，将其实现为一个类，把生成器函数放到iter代码里
from collections import deque


class linehistory:
    def __init__(self,lines,histlen=3):
        self.lines=lines
        self.history=deque(maxlen=histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append({lineno,line})
            yield line

    def clear(selfS):
        selfS.history.clear()

with open("test_file") as f:
    lines=linehistory(f)
    for line in lines:
        if 'python' in line:
            print('//////')


