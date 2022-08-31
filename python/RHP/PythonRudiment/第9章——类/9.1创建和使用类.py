#面向对象编程时最有效的软件编写方法之一。
#9.1 创建和使用类
#使用类几乎可以模拟任何东西。
#9.1.1 创建Dog类
#首字母大写的名称指的是类
# class Dog:
#     def __init__(self,name,age): #类似于构造方法
#         self.name=name
#         self.age=age
#
#     def sit(selfs):
#         print(f"{selfs.name} is now sitting.")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
#
#9.1.2 根据类创建实例
class Dog:
    '''...'''
    name=''
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"name={name},age={age}")
    print(f"name ={name},age={age}")
my_dog=Dog('willie',6)
#房屋内属性
print(my_dog.name)
print(my_dog.age)

your_dog=Dog('Lucy',3)
print(f"my dog name is {my_dog.name}")
print(f"your dog name is{your_dog.name}")

#test
class Resturant:
    name=''
    type=''
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def description(self):
        print(f"this rustaurant name is{self.name} and type is {self.type}")
    def open(self):
        print("working")

#调用餐馆的构造函数 给餐馆附默认值
rus=Resturant('luby','chinese')
#调用餐馆的描述函数
rus.description()
#调用餐馆的函数
rus.open()

rus2=Resturant('handa','indain')
rus3=Resturant('wos','amerian')

rus2.description()
rus3.description()

class User:
    first_name=''
    last_name=''

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def description(self):
        print(f"first_name is{self.first_name} and last_name is{self.last_name}")
    def greet_user(self):
        print('hello! how are you ?')

my_user=User('ren','haipeng')
my_user.description()
my_user.greet_user()
