#5.2.1 检查是否相等
car='bmw';
print(car=='bmw')  #检查等号两边的值是否相等

#5.2.2 检查是否相等时忽略大小写
#python对字符串大小写敏感
car='AUDI'
print(car=='audi')
#可以统一转化为大写/小写 然后再进行比较
print(car.lower()=='audi')

#5.2.3 检查是否不相等
requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")

#5.2.4数值比较
age=18
print(age==18)

#检查两个数不等
answer=17
if answer!=42:
    print("That is not the correct answer.Please try again!")

#检查多个条件
#要检查多个条件 可以使用and关键子将两个测试条件合二为一
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
age_1=22
print(age_0>=21 and age_1>=21)
#使用or关键字检查多个条件  只要满足其一就可以
age_0=22
age_1=18
print(age_0>=21 or age_1>=21)
age_0=18
print(age_0>=21 or age_1>=21)

#检查特定值是否包含再列表中  可以使用关键字 in
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoin' in requested_toppings)

#5.2.7 检察特定值是否包含在列表中
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users: #如果user 不在列表中
    print(f"{user.title()},you can post a reponse if you wish.")

#5.2.8 布尔表达式
game_active=True
can_edit=False
print(game_active,can_edit)

#Test
cars=['bmw','subaru','audi','benchi']
for car in cars:
    if car=='subaru':
        print("is car=='subaru'? I predicet Ture.")
    if car=='audi':
        print(" Is car=='audi'? I predice False.")
    else:
        print(car.title(),"都不是")

str_1='aaaa'
str_2='bbbb'
print(str_1==str_2,"直接比较")
str_2='Aaaa'
print(str_1.lower()==str_2.lower(),"统一转化为小写 进行比较")

number=20
print(number >=18,"是否成年")
print(number<=30,"而立之年")
print(number>24,"毕业了")
print(number<28,"结婚啦")

print(number>=18 and str_1.lower()=='aaaa',"and 关键字全部满足")
print(number>30 or  str_1.lower()=='aaaa',"or 关键子 只要满足一个")

numbers=[value for value in range(1,11)]
print("number",number)
print("numbers",numbers)
print(number in numbers)