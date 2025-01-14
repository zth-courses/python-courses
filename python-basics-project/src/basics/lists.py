# FILE: /python-basics-project/python-basics-project/src/basics/lists.py
# 该文件包含对列表基本操作的实现

def list_operations():
    # 元素计数
    fruits = ["苹果", "香蕉", "橙子", "苹果"]
    count = fruits.count("苹果")  # 统计元素出现次数
    print(f"苹果的数量: {count}")

    # 查找索引
    index = fruits.index("香蕉")  # 获取元素位置
    print(f"香蕉的索引: {index}")

    # 排序
    fruits.sort()            # 原地排序
    print(f"排序后的水果: {fruits}")

    # 反转列表
    fruits.reverse()         # 反转列表
    print(f"反转后的水果: {fruits}")

    # 复制列表
    new_fruits = fruits.copy()  # 创建新列表
    print(f"复制的水果列表: {new_fruits}")

    # 列表合并和扩展
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    # 合并列表
    combined = list1 + list2     # [1, 2, 3, 4, 5, 6]
    print(f"合并后的列表: {combined}")

    # 扩展列表
    list1.extend(list2)         # list1变为[1, 2, 3, 4, 5, 6]
    print(f"扩展后的列表1: {list1}")

    # 重复列表
    repeated = list1 * 2        # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    print(f"重复后的列表: {repeated}")

    # 列表推导式
    # 生成平方数列表
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    print(f"平方数列表: {squares}")

    # 带条件的列表推导式
    evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
    print(f"偶数列表: {evens}")