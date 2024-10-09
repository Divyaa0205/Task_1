class ToDoList:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, title):
        task = {"title":title,"completed":False}
        self.tasks.append(task)


