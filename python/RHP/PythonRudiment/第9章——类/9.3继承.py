# 一个类继承另一个类时，将自动获得另一个类的所有属性和方法
#9.3.1 子类的方法_init_()
#在即有类的基础上编写新类时，通常要调用父类的init，这将初始化在父类init方法中定义的所有属性，从而让子类包含这些属性
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year},{self.make},{self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can`t roll back odometer!")
    def increament_odometer(self,miles):
        self.odometer_reading+=miles
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}--km battery.")
    def get_range(self):
        if self.battery_size==100:
            range=315
    print(f"This car can go about {range} miles on a full charge.")


class ElectriCar(Car):
    def __init__(self,make,model,year):
        '''初始化父类属性'''
        super().__init__(make,model,year)
        '''设置自己独有的属性'''
        self.battery_size=75
        self.battery=Battery()
        #调用自己独有的方法
    def describe_battery(self):
        print(f"This car has a {self.battery_size}--km battery.")
    #重写父类的方法
    def fill_get_tank(self):
        print('This car doesn`t need a gas tank!')

my_tesla=ElectriCar('tesla','model`s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_get_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#Test
class Restaurant:
    def __init__(self,name,type='',icelist=''):
        self.name=name
        print(f"This restaurant name is {self.name}")

class IceCreamStand(Restaurant):
    '''初始化自己的属性'''
    def __init__(self,name,type,icelist):
        super().__init__(name,type,icelist)
        self.icelist=icelist
        self.name = name
        self.type = type
        '''调用父类的构造函数  进行初始化'''
    def pr(self):
        print(f"name={self.name} and icelist={self.icelist}")
icelist=['aaa','bbb','cccc']

icer=IceCreamStand('jj','ice',icelist)
icer.pr()


class User():
    def __init__(self,name,age,privieges):
        self.name=name
        self.age=age
        self.pri=privieges
    def description(self):
        print(f"this name={self.name} and age={self.age} and pri={self.pri}")

class Admin(User):
    def __init__(self,name,age,pri):
        self.name=name
        self.age=age
        super().__init__(name,age,pri)
        self.name=name
        self.age=age
        self.pri=pri
    def dec(self):
        print(f"this name={self.name} and pri={self.pri}")

ad=User('aa','bb',['ss','ooo','pp'])
ad.description()
ad=Admin('bb','vvv',['=','[','0'])
ad.description()

