#将列表存储在字典中，或将字典存在列表中
#6.4.1 字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]
for aline in aliens:
    print(aline)

#创建一个用于存储字典的列表
aliens=[]
#使用for循环创建字典
for aline_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien) #添加元素

#显示前5个
for alien in aliens[:5]:
    print(alien)
print("...")
#显示有多少数据
print(f" Total number of aliens:{len(aliens)}")

#更改前3个的数值
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

#显示前5个值
for alien in aliens[:5]:
    print(alien)
print("...")

#黄色改红色 速度快 值==15
for alien in aliens:
    if alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
    elif alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

print(aliens[:10])

#在字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print(f"You orderd a {pizza['crust']}-crust pizza""with the following toppings:")

for topping in pizza['toppings']: #直接在这里就开始列表的遍历
    print(f"\t+{topping}")

favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}`s favorite languages are:")
    if(len(languages)==1):
        print(languages[0])
        continue
    for language in languages:
        print(f"\t{language.title()}")

print(favorite_languages)

#6.4.3 在字典中存储字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

print(users)
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name=f"{user_info['first']}, {user_info['last']}"
    loaction=user_info['location']

    print(f"\t Full name:{full_name.title()}")
    print(f"\t Location:{loaction.title()}")

#Test
peoples={
    'aaa':{
        'name':'aaa',
        'age':16,
        'language':'python'
    },
    'bbb':{
        'name':'bbb',
        'age':20,
        'language':'java'
    },
    'ccc':{
        'name':'ccc',
        'age':30,
        'language':'php'
    }
}

for person in peoples.items():
    for man in person:
        print(man)

pet1={'type':'dog','owner':'aaa'}
pet2={'type':'cat','owner':'bbb'}
pet3={'type':'pig','owner':'ccc'}
pets={'pet1':pet1,'pet2':pet2,'pet3':pet3}

print(pets)
for pet,information in pets.items():
   print(f"pet={pet},information={information}")
   for seg in information.values():
       print(seg)

favorite_places={
    'aaa':['a1','a2','a3'],
    'bbb':['b1','b2','b3'],
    'ccc':['c1','c2','c3']
}
print(favorite_places)

for person in favorite_places:
    for place in favorite_places[person]:
        print(place)

cities={
    'shanaghai':{
        'persion':2000,
        'city':'china',
        'story':'old_shanghai'
    },
    'beijin':{
        'persion':5000,
        'city':'china',
        'story':'tiananmen'
    },
    'newyourk':{
        'persion':'?',
        'city':'usa',
        'story':'.....'
    }
}
for city in cities:
    print(cities[city])
    for image in cities[city]:
        print(cities[city][image])