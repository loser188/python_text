#可以使用类来模拟现实世界很多场景 可以在执行的任务时修改类的属性

#9.2.1

class Car:
    '''依次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
    def get_description_name(self):
        '''返回整洁的描述汽车的属性'''
        long_name=f'{self.year}{self.make}{self.model}'
        return  long_name.title()
my_new_car=Car('audi','a4',2019)
print(my_new_car.get_description_name())

#9.2.2
class Car:
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_desriptive_name(selfs):
        print(f"make={selfs.make} model={selfs.model}  year={selfs.year} odometer_reading={selfs.odometer_reading}")
    def read_odometer(self):
        '''打印一条指出汽车里程碑的信息'''
        print(f"This car has {self.odometer_reading} imles on it.")

    def update_odometer(selfs, mileage):
        selfs.mileage = mileage
        if mileage >= selfs.odometer_reading:
            selfs.odometer_reading=mileage
        else:
            print('You can`t roll back an odometer!')

    def increment_odometer(self,miles):
        self.odometer_reading+=miles


my_new_car=Car('audi','a4','2019')
print(my_new_car.get_desriptive_name())
my_new_car.read_odometer()

#9.2.3 修改属性的值
# class Car:
#     my_new_car=Car('audi','a4',2019)
#     print(my_new_car.get_desriptive_name())
#
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_used_car =Car('subaru','outback',2015)
print(my_used_car.get_desriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()










