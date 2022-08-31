#在迭代或其他形式的处理过程中对最后几项记录做有限的历史记录
from collections import deque


def search(lines,pattern,histroy=5):
    previous_lines=deque(maxlen=histroy)
    for line in lines:
        if pattern in line:
            yield  line,previous_lines
        previous_lines.append(line)

#
if __name__ == '__main__':
    with open('test_file') as f:
        for line,prevlines in search(f,"python",5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)

#Deque(max=N) 创建了一个固定长度的队列，当有记录加入队列而队列已满时，会自动移出最老的那条记录
q=deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(5)
print(q)

#如果不指定队列的大小，也就得到了一个无界限的队列
q=deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
q.popleft()


