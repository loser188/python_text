#使用if语句处理列表
#5.4.1检查特殊元素
requested_toppings=['mushrooms','green_peppers','extra_cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green_peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\n Finished making your pizza")

#5.4.2确定列表不是空
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}." )
    print("\n Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") #证明链表为空

    #if语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True,并在列表为空时，返回False

#5.4.3 使用多个列表
available_toppings=['mushrooms','olives','green_peppers','pepperoni',"pineapple",'extra_cheese']
requested_toppings=['mushrooms','french_fries','extra_cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don`t have {requested_topping}.")
print("\n Finshed making your pizza!")

#Test
persions=['loary','jeckey','polo','bobry','sandery','admin']
if persions:
    for persion in persions:
        if persion == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello,thank you for logging in again")

del persions

current_users=['boob','alise','admine','jiao','bish']
new_users=['aaa','bbb','alise','ddd','jiao']
for ne in new_users:
    if ne.lower() in current_users:
        print("姓名已存在",ne)
    else:
        print("用户名未使用",ne)
numbers=[val for val in range(1,10)]
for number in numbers:
    print(number)





