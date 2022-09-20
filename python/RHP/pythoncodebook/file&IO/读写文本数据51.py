# 对文本数据进行读写操作，但不同的文本，有不同的编码
# open()配合rt模块
with open("myFile.txt", encoding='utf-8') as f:
    date=f.read()
    print(date)

with open('myFile.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

# 写入操作  wt 模块   会清除原先的文本，并写入


# 文件结尾追加内容  at模块
with open('myFile.txt', 'at', encoding='utf-8') as f:
    f.write('//////')
    print(f)

# with会为使用的文件创建一个上下文环境，当程序离开这个with语句块时，文件会自动关闭

#关于换行符   unix和windows是不相同的，\n \r\n  python默认是通用换行符\n   如果不想换行  可以主动通过newline参数声明换行符