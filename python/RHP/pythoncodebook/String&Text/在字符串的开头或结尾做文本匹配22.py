# 我们需要在字符串的开头或结尾处按照指定的文本模式做检查，
# 使用str.startswith函数和str.endwith方法
import os

filename='spam.txt'
print(filename.endswith('.txt'))
# 如果需要同时针对多个选项做检查，只需要给startwith和endwith提供包含可能选项的元组即可

filename=os.listdir('.')
print(filename)
print([name for name in filename if name.endswith(('.c', '.py'))])

#可以通过将列表或或集合通过tuple函数转为元组进而进行完成函数传参



