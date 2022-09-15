# 构建自定义容器，内部对象是一个列表、元组或其他可迭代对象。
# 自定义一个iter()方法，将迭代请求委托到对象内部特有的容器上
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def _repr_(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
if __name__ == '__main__':
    root=Node(0)
    child1=Node(1)
    child2=Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)