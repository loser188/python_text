#python允许函数从调用语句中收集任意数量的实参
def make_pizza(*toppings):
    '''打印顾客点的所有配料。'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# 形参*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都分装到这个元组中。

def make_pizza(*toppings):
    print("\n making a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#8.5.1 结合使用位置实参和任意数量参数
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
def make_pizza(size,*toppings):
    print(f"\n making a {size}--inch pizza with the following toppings?")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.5.2 使用任意数量的关键字实参
#将函数编写成能够接受任意数量的键值对，调用语句提供了多少就接受多少。
def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

#test
def swindwitch(*pr):
    print(pr)
swindwitch('aaa','bbb','ccc')
swindwitch('111','sss')
gg={'aaa':'aaa'}
swindwitch(gg)

def user_profile(**kwargs):
    first=kwargs.get('first')
    print(first,"lllll")
    last=kwargs.get('last')
    print(last)
    mess=kwargs.get('mess')
    print(mess)
    ans=build_profile(first,last,mess)
    print(ans)


mess={'aaa':'aa','bbb':'bbb'}
ll={'first':'r','last':'hp','mess':mess}
user_profile(ll,mess,mess)


