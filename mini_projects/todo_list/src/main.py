
from task import Task
from todo_list import TodoList
def main():
    todo_list = TodoList()
    while True:
        print("1. 添加任务")
        print("2. 查看任务列表")
        print("3. 标记任务完成")
        print("4. 删除任务")
        print("5. 退出")

        choice = input("请选择操作：")
        if choice == "1":
            name = input("请输入任务名称：")
            description = input("请输入任务描述（可选）：")
            due_date = input("请输入截止日期（可选）：")
            priority = input("请输入优先级（可选）：")
            task = Task(name, description, due_date, priority)
            todo_list.add_task(task)
        elif choice == "2":
            tasks = todo_list.get_tasks()
            if tasks:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
            else:
                print("任务列表为空")
        elif choice == "3":
            index = int(input("请输入要标记完成的任务编号：")) - 1
            todo_list.mark_task_done(index)
        elif choice == "4":
            index = int(input("请输入要删除的任务编号：")) - 1
            todo_list.remove_task(index)
        elif choice == "5":
            break
        else:
            print("无效的选择，请重新输入")

if __name__ == '__main__':
    main()