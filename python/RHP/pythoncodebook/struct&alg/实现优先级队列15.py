#实现一个队列，它能够以给定的优先级来对元素排序，且每次POP操作时都会返回优先级最高的那个元素
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue =[]
        self._index=0

    def push(selfs,item,priority):
        heapq.heappush(selfs._queue,(-priority,selfs._index,item))
        selfs._index+=1

    def pop(selfs):
        return heapq.heappop(selfs._queue)[-1]
    #测试GIT推送