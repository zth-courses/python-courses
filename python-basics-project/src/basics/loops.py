# FILE: /python-basics-project/python-basics-project/src/basics/loops.py
# 该文件实现循环的基本用法，包括for循环和while循环的示例，以及如何使用循环遍历列表和字典。

def loop_examples():
    # for循环示例
    fruits = ["苹果", "香蕉", "橙子"]
    print("使用for循环遍历列表:")
    for fruit in fruits:
        print(fruit)

    # while循环示例
    count = 0
    print("使用while循环遍历列表:")
    while count < len(fruits):
        print(fruits[count])
        count += 1

    # 遍历字典
    student = {
        "name": "小红",
        "age": 20,
        "scores": {
            "语文": 90,
            "数学": 95
        }
    }
    print("遍历字典:")
    for key, value in student.items():
        print(f"{key}: {value}")

