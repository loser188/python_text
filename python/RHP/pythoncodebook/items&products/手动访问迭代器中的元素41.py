# 不使用for访问可迭代对象中的元素
# 手动访问迭代器中的元素，可以使用next函数，自己手动编写代码来捕获异常
with open("test_file") as f:
    try:
        while True:
            line =next(f)
            if line is None:
                break
            print(line,end=" ")
    except StopIteration:  # 用来通知迭代结束
        print("error")