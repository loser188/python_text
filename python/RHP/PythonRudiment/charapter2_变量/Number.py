#数

#2.4.1整数
print(2+3)   #加法
print(3-2)   #减法
print(2*3)   #乘法
print(3/2)   #除法

print(2**3) #两个连续的*号表示乘方
print(2+   3*4** 2) #支持算数优先级   空格不影响计算

#2.4.2 浮点数
print(0.1+0.1)
print(0.2+0.1)  #结果包含的小数位数可能不确定

#2.4.3 整数与浮点数
print(4/2)
print(1+2.0)  #精度向上转化

#2.4.4 数中下划线
universe_age=14_000_000_000  #数字很大 使用下划线进行连接  看起来清晰
print(universe_age)

#2.4.5 同时给多个变量赋值
x,y,z=0,1,2
print(x,y,z)

#2.4.6 常量
#python没有内置常量类型，一般全大写表示常量
MAX_CONNECTIONS=5000
print(MAX_CONNECTIONS)

#Test
print(3+5)
print(2*4)
print(9-1)
print(round(16/2))  #round 不传第二个参数 默认不保留小数

number=16
number="我最喜欢的数字"+str(number)  #使用str函数将number转化为字符串类型  然后进行拼接
print(number)
