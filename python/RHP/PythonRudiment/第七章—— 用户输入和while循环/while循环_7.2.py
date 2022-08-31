#for 循环用于针对集合中的每个元素都执行一个代码块，而while循环则不断运行，直到指定的条件不满足为止
#7.2.1 使用while循环
current_number=1
while  current_number<=5:
    print(current_number)
    current_number+=11

#7.2.2 让用户选择何时退出
# prompt='\nTell me something,and I will repeat it back to you;'
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

#7.2.3 使用标记
#不同的事情导致程序停止运行
#可以定义一个变量，用于判断整个程序是否处于活动状态，这个变量称为标记，充当程序的交通信号
# prompt = "\n Tell me sometjing,and I will repaet it back to you:"
# prompt+="\n Enter 'quit' to end the program."
# active=True
# while active:
#     message=input(prompt)
#
#     if message=='quit':
#         active=False
#     else:
#         print(message)


#7.2.4 使用break推出循环
# prompt="\n Please enter the name of a city you have visited"
# prompt+="\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city=input(prompt)
#
#     if city=='quit':
#         break
#     else:
#         print(f"I`d love to go to {city.title()}")

#7.2.5在循环中使用continue
#返回循环开头 继续执行
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#7.2.6 避免无限循环

#test
print("please input something ")
while True:
    flag=input()
    if flag=='quit':
        break
    else:
        print("please input again")









