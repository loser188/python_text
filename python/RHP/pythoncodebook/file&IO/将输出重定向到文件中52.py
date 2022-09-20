# 将print的输出重定向到文件中
with open("myFile.txt", 'wt',encoding='utf-8') as f:
    print('hello Word',file=f)
    print(f)