#传递参数
#函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
#多参数的情况下，可以有多种传递方式。1.位置参数，实参的顺序与形参循序相同 2.也可以使用关键字参数 每个实参都由变量名和值组成
#3 还可以是列表和字典

#8.2.1 位置参数 最简单的关联方式就是基于实参的顺序
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print(f"\n I hava a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")
describe_pet('hamster','harry')

#8.2.2 关键字实参
#关键字实参是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆。
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")
describe_pet(animal_type='hamster',pet_name='harry') #显示绑定

#8.2.3 默认值
#给定每个形参指定默认值。在调用函数中给形参提供了实参时，python将使用指定的实参值。否则将使用默认值。
def describe_pet(pet_name,animal_type='dog'):
    '''显示宠物的信息。'''
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")
describe_pet(pet_name='wille')
describe_pet('aaa') #按照位置参数绑定 默认第一个

#8.2.4 等效的函数调用
#8.2.5 避免实参错误

#Test
def make_shirt(size=0,words='aaa'):
    print("please input a size and one words!")
    size=int(input("a size="))
    words=input("one words!")
    print(f"\n The size={size} and the words={words}")
make_shirt(words='fff');

