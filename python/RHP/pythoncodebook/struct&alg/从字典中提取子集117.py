# 想创建一个子集，其本身是另外一个字典的子集
# 利用字典推导式
prices={
    'acms':45.23,
    'aapl':431,
    'ibm':205.55,
    'hpq':367
}

p1={key:value for key,value in prices.items() if value>200}
print(p1)

tech_names={'aapl','ibm','hpq'}
p2={key:value for key,value in prices.items() if key in tech_names}
print(p2)
