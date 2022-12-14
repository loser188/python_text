# 除去序列中出现的重复元素，但仍然保持剩下的元素顺序不变
# 如果序列中的值是可哈希的，那么这个问题可以通过使用集合和生成器解决

def dedupe(items,key=None):
    seen=set()
    for item in items:
        val = item if key is None else key(item) # 不可hash版本
        if item not in seen:  # 元素可以哈希
            yield item
            seen.add(item)

a=[1,4,2,5,7,4,3,7,0]
print(list(dedupe(a)))

# 不可hash版本中key的作用是指定一个函数用来将序列中的元素转换为可哈希的类型。

# 如果只是去重，那么通常足够简单的的办法去构建一个集合
a=[1,2,3,5,3,2,3,4,5,7,5,4,3]
print(set(a))
# 但这种方法不能保证元素顺序不变。