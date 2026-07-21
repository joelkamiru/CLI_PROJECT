class Task:    
    id_counter = 1  

    def __init__(self, title, project_title, status="Pending", assigned_to=None, task_id=None):
        self.title = title
        self.project_title = project_title
        self._status = status
        self.assigned_to = assigned_to

        if task_id:
            self.id = task_id
            if task_id >= Task.id_counter:
                Task.id_counter = task_id + 1
        else:
            self.id = Task.id_counter
            Task.id_counter += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["Pending", "In Progress", "Completed"]
        if value in allowed:
            self._status = value
        else:
            print(f"Invalid status! Allowed values: {allowed}")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "project_title": self.project_title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            project_title=data["project_title"],
            status=data["status"],
            assigned_to=data.get("assigned_to"),
            task_id=data["id"]
        )

    def __str__(self):
        return f"Task #{self.id}: [{self.status}] {self.title} (Project: {self.project_title})"