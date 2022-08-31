#使用字典
#字典是一系列键值对，每个键都与一个值关联，可以使用键来访问关联的值。与键关联的值可以是数、字符串、列表和字典。
#在python中使用”{}“标识字典
#键和值之间使用”：“分隔开

#6.2.1访问字典中的值
#获取与键想关联的值，可以依次指定字典名和放在方括号内的值
alien_0={'color':'green'}
print(alien_0['color'])

alien_0={'color':'green','points':5}
new_points=alien_0['points']
print(f"You just earned {new_points} points!")

#6.2.2添加键值对
#字典是一个动态结构，可以随时添加键值对。依次指定字典名、使用方括号括起的键和相关的值
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0  #添加x坐标
alien_0['y_position']=25  #添加y坐标
print(alien_0)

#6.2.3 先创建一个空字典
#在空字典中添加键值对
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#6.2.4 修改字典中的值
#可以依次指定字典名、用方括号括起的键，以及与该键关联的新值
alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")
#向右移动
#根据当前速度，移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:#移速很快
    x_increment=3
alien_0['x_position']+=x_increment
print(f"New position :{alien_0['x_position']}")

#6.2.5 删除键值对
#可以使用del语句将相应的键值对彻底删除，使用del语句时，必须指定字典名和要删除的键
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)


#6.2.6 由类似对象组成的字典
#字典可以存储一个人的多种信息，也可以存储多个人的同一种信息
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

language=favorite_languages['sarah'].title()
print(f"Sarah`s favorite language is {language}.")

#6.2.7使用Get来访问值
alien_0={'color':'green','speed':'slow'}
#print(alien_0['points'])
point_value=(alien_0.get('points','No point value assigned.'))
print(point_value)

#test
persion={'first_name':'R','last_name':'hp','age':23,'city':'xian'}
print(persion)

love_number={'rhp':14,'aaa':0,'bbb':23,'kkk':18,'hhh':20}
for number in love_number:
    print(f"{number} is love {love_number[number]}!")

kills={"oop":"面向对象","RPC":"微服务","FAUST":"api调用风格",'云原生':"flink"}
for kill in kills:
    print(f"{kill} : {kills.get(kill)}")