class Task:

    id_counter = 1

    def __init__(self, title, project_title, status="Pending", assigned_to="", task_id=None):
        if task_id is not None:
            self.id = int(task_id)
            if self.id >= Task.id_counter:
                Task.id_counter = self.id + 1
        else:
            self.id = Task.id_counter
            Task.id_counter += 1

        self.title = title
        self.project_title = project_title
        self.status = status
        self.assigned_to = assigned_to

    def __str__(self):
        return f"Task #{self.id}: {self.title} [{self.status}]"