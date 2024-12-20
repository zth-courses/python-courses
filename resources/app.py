msg = "雷猴x1000"
print(msg)
print(10//3)
print(10/3)
print(10%3)
print(10**3)
age = 18
if age >= 18:
  print("成年")
else:
  print("未成年")

# 条件运算符
# and 与
# or 或
# not 非
# 实现一个案例
def greet(name):
    print(f"欢迎，{name}!")

greet("小明")


# list 列表

book_list = ["三国演义", "水浒传", "西游记", "红楼梦"]
print(book_list[0])

# 循环
for book in book_list:
	print(book)

# 操作列表的方法
book_list.append("语文") # 添加元素
print(len(book_list)) # 获取列表长度
book_list.insert(0, "数学") # 在指定位置插入元素
print(book_list)
book_list.remove("数学") # 删除指定元素
print(book_list)
book_list.pop(0) # 删除指定位置的元素
print(book_list)


# 元组 tuple
pokemons = ("皮卡丘", "杰尼龟", "小火龙")
print(pokemons[0])

# 字典 dict
student = {"name": "小明", "age": 18, "gender": "男"}
print(student["name"])

# 集合 set
s = {1, 2, 3, 4, 5}
print(s)

# 函数
def add(a, b):
    print(a + b)
    return a + b

print(add(1, 2))


# 引入模块
# 一些常用标准库的简单示例

# 日期时间处理
from datetime import datetime
print(datetime.now())

# 随机数生成
import random
print(random.randint(1, 100))

# 文件路径操作
import os
print(os.getcwd())  # 获取当前工作目录
print(os.listdir("."))
# JSON处理
import json
data = {'name': '张三', 'age': 25}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 数学计算
import math
print(math.pi)
print(math.sqrt(16))

# 正则表达式
import re
text = "我的电话是123-4567-8900"
phone = re.search(r'\d{3}-\d{4}-\d{4}', text)
print(phone.group())

# 创建一个car类
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.brand} {self.model} 已经启动")

car = Car("Toyota", "Prius", 2024)
car.start()
# 修改类属性
car.brand = "Honda"
print(car.brand)

# 创建一个继承Car类的子类
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
        
    # 重写start方法
    def start(self):
        print(f"{self.brand} {self.model} 已经启动，电池容量为{self.battery_size}kWh")
          
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电")

electric_car = ElectricCar("Tesla", "Model 3", 2024, 100)
electric_car.charge()
electric_car.start()
