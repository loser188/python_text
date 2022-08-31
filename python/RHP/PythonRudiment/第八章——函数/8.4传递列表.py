
def greet_users(names):
    '''向列表中的每位用户发出简单的问候'''
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)

usernames=['hannah','ty','margot']
greet_users(usernames)

#8.4.1 在函数中修改列表
#将列表传递给函数后，函数就可对齐进行修改。而且时永久性的修改
unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"printing model:{current_design}")
    completed_models.append(current_design)

print("\n The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"print model:{current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#8.4.2 禁止函数修改列表
print_models(unprinted_designs[:],completed_models)
print(completed_models)

#test
messages=['hello','aaa','what it is?','so how about it ?']
def show_message(messages):
    for mes in messages:
        print(mes)
show_message(messages)

sent_message=[]
def send_messages(mess,sent_mess):
    while mess:
        tmpmes=mess.pop()
        tmp_sent_mess=sent_mess.append(tmpmes)
    print(f"the msee = {sent_mess}")

send_messages(messages,sent_message)

print("传递副本")
