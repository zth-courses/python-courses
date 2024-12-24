# Python更多基础语法示例

# 1. 元组操作（不可变序列）
coordinates = (10, 20)  # 创建元组
x, y = coordinates      # 元组解包

# 2. 集合操作
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)    # 交集
print(set1 | set2)    # 并集
print(set1 - set2)    # 差集

# 3. 字符串操作
text = "Python编程"
print(text.upper())      # 转大写
print(text.replace("Python", "Java"))  # 替换
print("程序" in text)    # 包含判断
print(text.split("n"))   # 分割字符串

# 4. 生成器和迭代器
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 5. 装饰器
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def greet(name):
    return f"你好, {name}!"

# 6. lambda表达式
square = lambda x: x**2
print(square(5))

# 7. map/filter/reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x*2, numbers))  # [2,4,6,8,10]
filtered = list(filter(lambda x: x>2, numbers))  # [3,4,5]
reduced = reduce(lambda x,y: x+y, numbers)  # 15

# 8. 列表/字典/集合推导式
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}
matrix = [[i+j for j in range(3)] for i in range(3)]

# 9. 上下文管理器
class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文")

# 10. 模块导入方式
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn

# 11. 多重继承
class A:
    def method(self):
        print("A方法")

class B:
    def method(self):
        print("B方法")

class C(A, B):
    pass

# 12. 正则表达式
import re
pattern = r'\d+'
text = "我的电话是123456"
numbers = re.findall(pattern, text)

# 13. 异步编程
import asyncio

async def async_function():
    await asyncio.sleep(1)
    return "完成"

# 14. 类型注解
from typing import List, Dict

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# 15. 属性装饰器
class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value