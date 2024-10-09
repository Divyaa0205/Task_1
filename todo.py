class ToDoList:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, title):
        task = {"title":title,"completed":False}
        self.tasks.append(task)

    def complete_task(self,task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['Completed'] = True

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id)

