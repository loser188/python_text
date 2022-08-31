#使用while处理列表和字典
#for循环水是一种有效的遍历方式，但是不应该在for循环中修改列表
#7.3.1 在列表之间移动元素
#首先，创建一个等待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#7.3.2 删除为特定值的所有列表元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#7.3.3 使用用户输入来填充字典
pesponses={}
#设置一个标志，指出调查是否继续
polling_active=True

while polling_active:
    #提示输入被调查者的名字和回答
    name=input("\n what is your name? ")
    response = input("which mountain would you like to climb someday?")
    #看看是否还有人要参与调查
    repeat=input("would you like to let another persion respond? (yes/n)")
    if repeat=='no':
        polling_active=False
    #调查结束，显示结果
    print("\n--- Poll results --")
    for name,response in response.items():
        print(f"{name} would like to climb {response}.")