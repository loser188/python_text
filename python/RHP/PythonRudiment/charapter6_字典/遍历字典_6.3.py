#遍历字典
#python可以遍历所有的键值对，也可以仅遍历键或值

#6.3.1 遍历所有键值对
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
#使用for循环遍历字典
for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")
#简单命名
for k,v in user_0.items():
    print(f"\n{k},{v}")

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name ,language in favorite_languages.items():
    print(f"{name.title()}`s favorite language is {language.title()}.")

#6.3.2 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
#遍历字典时，会默认遍历所有的键、
for name in favorite_languages:
    print(name.title())
for name in favorite_languages.keys():
    print(name.title())

friends=['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\n{name.title()},I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll！")

#6.3.3 按照特定顺序遍历字典中所有的键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}，thank you for taking the poll.")

#6.3.4遍历字典中所有的值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#为了去重，可以使用集合（set），集合中的每个元素都时独一无二的。
print("The flowing languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#Test
for n,v in favorite_languages.items():
    print(f"{n},{v}")

favorite_languages['number']='数字'
favorite_languages[ 'liet']='列表'
favorite_languages[ 'dict']='字典'
favorite_languages[ 'for']='循环'
favorite_languages[ '[]']='元组'
print(favorite_languages)
for k,v in favorite_languages.items():
    print(f"{k},{v}")

rivers={'nile':'egypt','sss':'daa','www':'ffff'}
for river in rivers:
   print(f"{river} runs through {rivers.get(river)}")

