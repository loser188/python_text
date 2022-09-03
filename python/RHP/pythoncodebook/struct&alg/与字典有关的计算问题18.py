# 想在字典上对数据做各式各样的计算（最大、最小、排序）
prices={
    'acme':45.23,
    'aapl':612.78,
    'ibm':37.20,
    'hpq':10.5,
    'aaa':10.5
}

# 为了能对字典内容做一些有用的计算，通常会利用zip将字典的键值反转过来。

min_price=min(zip(prices.values(),prices.keys()))
print(min_price)

max_price=max(zip(prices.values(),prices.keys()))
print(max_price)

# 对数据排序，使用zip再配合sorted()就可以了
prices_sorted=sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)

# zip函数创建了一个迭代器，内容只能被消费一次

# 在字典上执行常规的操作，只会处理键，而不是值。
# 遇到value-key有多个相同的key时，max会返回第一个 而 min会返回最后一个
