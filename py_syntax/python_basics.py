# Python基础语法示例

# 1. 变量和数据类型
name = "小明"  # 字符串
age = 18       # 整数
height = 1.75  # 浮点数
is_student = True  # 布尔值

# 2. 列表操作
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("草莓")  # 添加元素
fruits.pop()          # 删除最后一个元素
first_fruit = fruits[0]  # 访问元素
fruits.remove("香蕉") # 删除某一个元素 

# 3. 字典操作
student = {
    "name": "小红",
    "age": 20,
    "scores": {
        "语文": 90,
        "数学": 95
    }
}

# 4. 条件语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 5. 循环
# for循环
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# while循环
count = 0
while count < 3:
    print(f"当前计数：{count}")
    count += 1

# 6. 函数定义
def calculate_average(numbers):
    """计算平均值的函数"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 函数使用示例
scores = [80, 90, 75, 85]
average = calculate_average(scores)
print(f"平均分：{average}")

# 7. 类的定义
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁"

# 类的使用
student1 = Student("小华", 16)
print(student1.introduce())

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