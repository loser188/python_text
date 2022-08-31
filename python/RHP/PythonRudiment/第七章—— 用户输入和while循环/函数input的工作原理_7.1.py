#7.1 函数input的工作原理
#函数input让程序暂停运行，等待用户输入一些文本。
# message=input('Tell me something,and I will repeat it back to you :')
# print(message)
#7.1.1 编写清晰的程序
#使用input函数时，都应该指定清晰易懂的提示
# name=input("Please enter your name:")
# print(f"\nHello ,{name}!")
#提示信息超过一行
# promt='If you tell us who you are , we can personalize the messages you s'
# promt+="\nWhat is your first name?"
#
# name=input(promt)
# print(f"\nHello,{name}!")
#7.1.2 使用int()来获取数值输入
# age=input("How old are you ？")
# print(age)
# age=int(age)
# print(age>=18)
#
# height=input("How tall are yiou, in inches?")
# height=int(height)
#
# if height>=48:
#     print("\nYou`re tall enough to ride!")
# else:
#     print("\n You`ll be able to ride when you`re a little older.")

#7.1.3求模运算
#%运算是一个很有用的工具，将两个数相除并返回余数
# print(4%3)
# print(5%3)
# print(6%3)
# print(7%3)
#取模运算不会指出一个数是另一个数的多少倍，只指出余数是多少。
#利用余数判断是奇/偶数
# number=input("Enter a number,and I`ll tell you if it`s even or odd:")
# number=int(number)
#
# if number%2==0:
#     print(f"\n The number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# 汽车租赁
print("what kind or car you like?")
car=input()
print(f"Let me see if I can find you a {car}")

# 餐馆订位
print("how many people wile coming in?")
people_numbers=input()
if  int(people_numbers)>8:
    print(f"the people_number is{people_numbers} and over 8,didn`t have enough table")
else:
    print("there are one table to using ")

#10的整数倍
print("please input a number")
number=input()
if int(number)%10 == 0:
    print("是10的倍数")
else:
    print("不是10的倍数")
