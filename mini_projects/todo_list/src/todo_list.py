# 待办事项列表类，包含任务添加、删除、标记完成等方法

from utils import read_file, write_file
class TodoList:
    file_path = 'tasks.txt'
    def __init__(self):
        """
        初始化待办事项列表。
        """
        self.tasks = read_file(self.file_path) or []
    def add_task(self, task):
        """
        添加任务。
        参数：
        - task (Task): 要添加的任务对象。
        """
        self.tasks.append(task)
        write_file(self.file_path, task)
    def remove_task(self, index):
        """
        根据索引删除任务。

        参数：
        - task (Task): 要删除的任务对象。
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("索引超出范围")
        del self.tasks[index]
        tasks_str = '\n'.join(str(x) for x in self.tasks)
        write_file(self.file_path, tasks_str)
    def mark_task_done(self, index):
        """
        标记任务为已完成。
        参数：
        - task (Task): 要标记为已完成的任务对象。
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("索引超出范围")
        self.tasks[index].is_done = True
        write_file(self.file_path, self.tasks)
    def get_tasks(self):
        """
        获取待办事项列表中的所有任务。

        返回值：
        - list: 待办事项列表中的所有任务。
        """
        return self.tasks