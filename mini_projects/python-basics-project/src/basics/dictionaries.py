# FILE: /python-basics-project/python-basics-project/src/basics/dictionaries.py
# 字典的基本操作示例

# 创建字典
student = {
    "name": "小红",
    "age": 20,
    "scores": {
        "语文": 90,
        "数学": 95
    }
}

# 访问字典元素
def access_elements():
    print("姓名:", student["name"])  # 输出: 小红
    print("年龄:", student.get("age"))  # 输出: 20
    print("语文成绩:", student["scores"]["语文"])  # 输出: 90

# 添加键值对
def add_key_value():
    student["gender"] = "女"  # 添加性别
    print("添加性别:", student)

# 更新值
def update_value():
    student["age"] = 21  # 更新年龄
    print("更新年龄:", student)

# 删除键值对
def delete_key_value():
    del student["scores"]["数学"]  # 删除数学成绩
    print("删除数学成绩:", student)

# 遍历字典
def iterate_dictionary():
    for key, value in student.items():
        print(f"{key}: {value}")

# 主函数
if __name__ == "__main__":
    access_elements()
    add_key_value()
    update_value()
    delete_key_value()
    iterate_dictionary()