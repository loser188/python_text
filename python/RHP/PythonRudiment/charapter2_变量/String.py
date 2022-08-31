#字符串
#python中 使用引号括起来的都是字符串 包括单引号 双引号

message_2="This is a String"
print(message_2)

message_2='This is also a String'
print(message_2)

message_2='I told my firend,"Python is my favorite language!"' #单引号中包含双引号
print(message_2)

message_2="The language 'Python' is named after Monty Python ,not the snake."\
"One of Python`s Strengths is its diverse and supportive community."
print(message_2)

message_2="mmmm""oooo"   #在Python 看来  两侧的双引号是配对的  中间的是单独的  在编译阶段  是最近配对的
print(message_2)

#2.3.1 使用方法修改字符串的大小写
name="ada lovelace"
print(name.title(),"使用字符串自带的方法 将首字母大写")
print(name.upper(),"全部改为大写")
print(name.lower(),"全部改为小写")

#2.3.2 在字符串中使用变量
first_name="ada"
last_name="lovelace"
full_name=f"{first_name}{last_name}" #要在字符串中插入变量的值，可在前引号前加上字符f，再将要插入的变量放入花括号内 f=formate 3.6=f  3.5=formate
print(full_name)
print(f"Hello,{full_name}")

#2.3.3 使用制表符或换行符来添加空白
print("python")
print("\t python",'使用制表符空4格')
print("Languages:\nPython\nC\nJavaScript",'使用n进行换行')
print("Languages:\n\tpython\n\tC\n\tJaveScript",'同时使用制表符进而换行符')

#2.3.4 删除空白
#python 能够找出字符串开头和结尾的多余空白
favorite_language='python  '
print(favorite_language,len(favorite_language))
favorite_language=favorite_language.rstrip()#使用rstrip函数去掉末尾空白 记得要关联回原字符
print(favorite_language,len(favorite_language))


favorite_language='   python     '
print(favorite_language,len(favorite_language))
# favorite_language=favorite_language.rstrip()  #去除右边的空白
# print(favorite_language,len(favorite_language))
#
# favorite_language=favorite_language.lstrip()  #去除右边的空白
# print(favorite_language,len(favorite_language))

favorite_language=favorite_language.strip()  #同时去除两边的空白
print(favorite_language,len(favorite_language))


#Test
name='RHP'  #设置人名
print("Hello RHP would you like to learn some Python today?")  #向其显示消息
lname=name.lower()  #全小写
uname=name.upper()  #全大写
tname=name.title()  #首字母大写
print(f'{lname},{uname},{tname}')  #以不同的形式展示名字
old_world="  \"生而为人，我用python.\"  "
print(name,"once side,",old_world)  #打印人名和名言

famous_persion=name
message=old_world
print(famous_persion,"once side,",message)  #赋值famoue_persion 和message

new_persion="     \tL.Rouse.Jeck   "
print(new_persion,len(new_persion))
# new_persion=new_persion.strip()  #去除名字两边的空白
# print("\n",new_persion)

new_persion=new_persion.rstrip() #去除右边的空白
print(new_persion,len(new_persion))
new_persion=new_persion.lstrip() #去除左边的空白
print(new_persion,len(new_persion))






