class Project:    
    id_counter = 1 

    def __init__(self, title, user_name, description="", due_date="N/A", project_id=None):
        self.title = title
        self.user_name = user_name
        self.description = description
        self.due_date = due_date

        if project_id:
            self.id = project_id
            if project_id >= Project.id_counter:
                Project.id_counter = project_id + 1
        else:
            self.id = Project.id_counter
            Project.id_counter += 1

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "user_name": self.user_name,
            "description": self.description,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            user_name=data["user_name"],
            description=data.get("description", ""),
            due_date=data.get("due_date", "N/A"),
            project_id=data["id"]
        )

    def __str__(self):
        return f"Project #{self.id}: '{self.title}' (Owner: {self.user_name})"