# 任务类，包含任务名称、描述、截止日期、优先级等属性
class Task:
    def __init__(self, name:str, description="", due_date="", priority="medium"):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_done = False
    def __str__(self):
        """
        返回任务的字符串表示形式。

        返回值：
        - str：任务的字符串表示形式，格式为“状态-任务名称（优先级：优先级，截止日期：截止日期）”。
        """
        # 如果任务已完成，状态为“√”，否则为“×”
        status = "✔️" if self.is_done else "❌"
        # 返回任务的字符串表示形式
        return f"{status} {self.name} (Priority: {self.priority}, Due Date: {self.due_date})"
    