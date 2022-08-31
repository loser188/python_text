#if 语句的简单示范
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper()) #如果是宝马就大写输出
    else:
        print(car.title())