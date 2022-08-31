#if 语句
#5.3.1 简单if语句
age =19
if age>=18:
    print('You are old enough to vote!')

age=19
if age>=18:
    print('You are old enough to vote!')
    print("Have you registered to vote yet?")
#5.3.2 if_else语句
age=17
if age>=18:
    print("You are old enougth to vote!")
    print("Have you registeed to vote yet?")
else:
    print('Sorry,you are too young to vote.')
    print('please register to vote as soon as you turn 18!')

#if_elif_else 结构
#检查超过两个条件的情况
age=12
if age<4:
    print('Your admission cost is $0.')
elif age<18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')
#简洁写法
age=12
if age<4:
    price=0
elif age<18:
    price=25
else:
    price=40
print(f"admission cost is{price}")

#5.3.4 使用多个elif 代码块

age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f" Your admission cost is{price}")

#python 并不要求if_elif后必须有else
age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"Your admission cost is {price}")

#5.3.6 测试多个条件
request_toppings=['mushrooms','estra cheese']
if 'mushrooms' in request_toppings:
    print('Adding mushrooms.')
if 'pepperoin' in request_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in request_toppings:
    print('Adding extra cheese.')
print("\n Finished making your pizza!")

#if_else 一旦条件成立，后续的条件就不会判断了

#Test
colors=['green','yellow','red']
score=0
for color in colors:
    allien_color = color
    if (allien_color == 'green'):
        score+=5
        print("The allien_color is Green",score)
    elif (allien_color=='yellow'):
        score+=10
        print("The allien_coloe is Green",score)
    elif(allien_color=='red'):
        score+=15
        print('The allien_color is Green',score)

ages=[age for age in range(1,100)]
for age in ages:
    if(age<2):
        print("这是婴儿",age)
    elif(age>=2 and age<4):
        print("这是幼儿",age)
    elif(age>=4 and age<13):
        print("这是儿童",age)
    elif(age>=13 and age<20):
        print("这是青少年",age)
    elif(age>=20 and age<65):
        print("这是成年人",age)
    else:
        print("这是老人",age)

fruits=['🍎','🍍','🍌','🍉']
if '🍎' in fruits:
    print("You really like apple")

