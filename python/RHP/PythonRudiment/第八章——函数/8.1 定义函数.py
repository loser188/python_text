#定义函数
#函数是带名字的代码块，用于完成具体的工作
def greet_user(): #向python指出了函数名字
    '''显示简单的问候语'''
    print('Hello!') #函数内部会做的事情
greet_user()

#8.1.1 向函数传递信息
def greet_user(username):
    '''显示简单的问候语。'''
    print(f"Hello,{username.title()}!")
greet_user('jesse')

#8.1.2实参和形参
#在greet_user函数中，username是一个形参，即函数完成工作所需的信息
#在greet_user('jesse')是一个实际参数

#test
def display_message():
    print("one words")
display_message()

def favorite_book(title):
    print(f"the {title} is book")
favorite_book('草上飞')