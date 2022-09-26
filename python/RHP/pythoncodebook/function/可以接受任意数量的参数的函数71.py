# 可以使用以*开头的参数
def avg(first,*rest):
    return (first+sum(rest))/(1+len(rest))

# rest是一个元组

print(avg(1, 2))
print(avg(1, 2, 3, 4))