#函数并非总是直接显示输出，它可以处理一些数据，并返回一个或一组值

#8.3.1 返回简单值
# def get_formatted_name(first_name,last_name):
#     '''返回整洁的姓名'''
#     full_name=f'{first_name} {last_name}'
#     return full_name.title()
# musician=get_formatted_name('jimi','hendrix')
# print(musician)

#8.3.2 让实参变成可选的
#可以使用默认值来让实参变成可选的
# def get_formatted_name(first_name,middle_name,last_name):
#     '''返回整洁的姓名'''
#     full_name=f"{first_name} {middle_name} {last_name}"
#     return  full_name.title()
# musician=get_formatted_name('john','lee','hooker')
# print(musician)

#给函数默认值  让其变为可选参数
def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:  #python 将非空字符串表示为true
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

musician=get_formatted_name('john','hooker','lee')
print(musician)

#8.3.3 返回字典
#函数可以返回任何类型的值，包括列表和字典等较为复杂的数据结构
def build_persion(first_name,last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person={'first':first_name,'last':last_name}
    return person
musician=build_persion('jimi','hendrix')
print(musician)

#扩展函数 加入可选参
def build_persion(first_name,last_name,age=None):
    '''返回一个字典，其中包含有关一个人的信息。'''
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_persion('jimi','hemdrix',age=27)
print(musician)
musician=build_persion('xxx','aaa')
print(musician)

#8.3.4 结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name=f"{first_name} {last_name}"
    return  full_name.title()
    #这是一个无限循环！
# while True:
#      print("\n please tell me your name:")
#      f_name=input('first name:')
#      l_name=input('last name:')
#
#      formatted_name=get_formatted_name(f_name,l_name)
#      print(f"\n Hello,{formatted_name}!")

#test
def city_country(city_name=None,city_countr=None):
    str=f"{city_name} {city_countr}"
    print(str)
out=city_country('上海')
print(out)
out=city_country( city_countr= 'aaa')
print(out)
out=city_country('aaa','bbb')
print(out)

def make_album(er_name,ed_name):
    '''歌手和专辑字典'''
    if er_name and ed_name:
        sing={'er':{er_name},'ed':{ed_name}}
    print(sing)

make_album('aaa','bbbb')

#增加专辑数
def make_album(er_name,ed_name,count=None):
    if count:
        sign={'er':{er_name},'ed':{ed_name},'count':{count}}
    else:
        sign={'er':{er_name},'ed':{ed_name}}
    print(sign)

make_album('xx','yyy','sadasd')
make_album('ccc','vvvv')
