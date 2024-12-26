# Python基础语法示例

# 1. 变量和数据类型
name = "小明"  # 字符串
age = 18       # 整数
height = 1.75  # 浮点数
is_student = True  # 布尔值

# 2. 列表操作
fruits = ["苹果", "香蕉", "橙子"]

# 添加元素
fruits.append("草莓")      # 在末尾添加：["苹果", "香蕉", "橙子", "草莓"]
fruits.insert(1, "梨")     # 在指定位置添加：["苹果", "梨", "香蕉", "橙子"]

# 删除元素
fruits.pop()              # 删除并返回最后一个元素
fruits.pop(1)            # 删除并返回指定位置的元素
fruits.remove("香蕉")     # 删除第一个匹配的元素
del fruits[0]            # 删除指定位置的元素

# 访问元素
first = fruits[0]        # 获取第一个元素
last = fruits[-1]        # 获取最后一个元素

# 切片操作
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])      # [1, 2, 3]
print(numbers[:3])       # [0, 1, 2]
print(numbers[2:])       # [2, 3, 4, 5]
print(numbers[::2])      # [0, 2, 4] (步长为2)

# 常用列表方法

fruits = ["苹果", "香蕉", "橙子"]

# 列表长度
length = len(fruits)     # 3

# 元素计数
count = fruits.count("苹果")  # 统计元素出现次数

# 查找索引
index = fruits.index("香蕉")  # 获取元素位置

# 排序
fruits.sort()            # 原地排序
fruits.reverse()         # 反转列表

# 复制列表
new_fruits = fruits.copy()  # 创建新列表



# 列表合并和扩展

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 合并列表
combined = list1 + list2     # [1, 2, 3, 4, 5, 6]

# 扩展列表
list1.extend(list2)         # list1变为[1, 2, 3, 4, 5, 6]

# 重复列表
repeated = list1 * 2        # [1, 2, 3, 1, 2, 3]

# 列表推导式

# 生成平方数列表
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 带条件的列表推导式
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]



# 3.字典的基本操作
student = {
    "name": "小红",
    "age": 20,
    "scores": {
        "语文": 90,
        "数学": 95
    }
}

# 访问字典元素
print(student["name"])  # 输出: 小红
print(student.get("age"))  # 输出: 20
print(student["scores"]["语文"])  # 访问嵌套字典，输出: 90

# 修改字典元素
student["age"] = 21
student["scores"]["英语"] = 88  # 添加新的成绩

# 检查键是否存在
if "name" in student:
    print("存在name键")

# 获取所有键和值
print(student.keys())    # 获取所有键
print(student.values())  # 获取所有值
print(student.items())   # 获取所有键值对

# 4. 条件语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 多条件判断
age = 25
income = 10000
if age > 18 and income > 5000:
    print("符合贷款条件")

# 三元运算符写法
status = "成年" if age >= 18 else "未成年"

# 逻辑运算符
# and, or, not的使用
is_weekend = True
is_holiday = False
has_guarantee = True

if is_weekend or is_holiday:
    print("可以休息")

if not is_holiday:
    print("需要工作")

# 多条件组合
if (age >= 18 and income > 5000) or has_guarantee:
    print("可以申请贷款")

# 5. 循环
# for循环
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 遍历范围
for i in range(5):    # 0到4
    print(i)

# 遍历字典
student = {"name": "小明", "age": 18}
for key in student:
    print(f"{key}: {student[key]}")

# 同时获取索引和值
for index, fruit in enumerate(fruits):
    print(f"第{index+1}个水果是{fruit}")

# 基本while循环
count = 0
while count < 3:
    print(f"当前计数：{count}")
    count += 1

# 带条件的while循环
password = ""
while password != "123456":
    password = input("请输入密码：")
    
# 无限循环
while True:
    user_input = input("输入'q'退出：")
    if user_input == 'q':
        break

# break: 跳出整个循环
for i in range(5):
    if i == 3:
        break
    print(i)  # 只打印0,1,2

# continue: 跳过当前迭代
for i in range(5):
    if i == 2:
        continue
    print(i)  # 打印0,1,3,4

# else子句（循环正常完成时执行）
for i in range(3):
    print(i)
else:
    print("循环正常结束")

# 嵌套循环
# 打印乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行

# 带break的嵌套循环
for i in range(3):
    for j in range(3):
        if i == j == 1:
            break
        print(f"i={i}, j={j}")

# 列表推导式（替代简单循环）
# 传统for循环
squares = []
for x in range(5):
    squares.append(x**2)

# 使用列表推导式
squares = [x**2 for x in range(5)]

# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]


# 6. 函数定义
def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    参数:
        numbers: 数字列表
    
    返回:
        float: 平均值，如果列表为空返回0
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 函数使用示例
scores = [80, 90, 75, 85]
average = calculate_average(scores)
print(f"平均分：{average}")

# 7. 类的定义
class Student:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁"

# 类的使用
student1 = Student("小华", 16)
print(student1.introduce())

# 类属性和实例属性
class Student:
    # 类属性（所有实例共享）
    school = "第一中学"
    
    def __init__(self, name, age):
        # 实例属性（每个实例独有）
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name}来自{self.school}"

# 访问类属性
print(Student.school)  # 输出：第一中学

# 访问实例属性
student = Student("小红", 17)
print(student.name)  # 输出：小红

# 私有属性和方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # 私有属性
    
    def __calculate_grade(self):  # 私有方法
        if self.__score >= 90:
            return "A"
        elif self.__score >= 60:
            return "B"
        return "C"
    
    def get_grade(self):
        return f"{self.name}的等级是{self.__calculate_grade()}"

student = Student("小华", 95)
print(student.get_grade())  # 输出：小华的等级是A
# print(student.__score)  # 错误：无法直接访问私有属性

# class继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是{self.name}"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 调用父类构造函数
        self.grade = grade
    
    def introduce(self):  # 重写父类方法
        return f"{super().introduce()}，我在{self.grade}年级"

student = Student("小明", 15, "初三")
print(student.introduce())  # 输出：我是小明，我在初三年级

# 类方法和静态方法
class Student:
    count = 0  # 类属性
    
    def __init__(self, name):
        self.name = name
        Student.count += 1
    
    @classmethod
    def get_student_count(cls):  # 类方法
        return f"当前学生数量：{cls.count}"
    
    @staticmethod
    def is_adult(age):  # 静态方法
        return age >= 18

# 使用类方法和静态方法
print(Student.get_student_count())  # 输出：当前学生数量：0
print(Student.is_adult(20))  # 输出：True

# 8. 异常处理
try:
    number = int("abc")
except ValueError:
    print("转换失败：请输入有效的数字")

# 9. 文件操作
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("这是一个测试文件")

# 10. 列表推导式
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]