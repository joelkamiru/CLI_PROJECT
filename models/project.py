class Project:

    id_counter = 1

    def __init__(self, title, user_name, description="N/A", due_date="N/A", project_id=None):
        if project_id is not None:
            self.id = int(project_id)
            if self.id >= Project.id_counter:
                Project.id_counter = self.id + 1
        else:
            self.id = Project.id_counter
            Project.id_counter += 1

        self.title = title
        self.user_name = user_name
        self.description = description if description else "N/A"
        self.due_date = due_date if due_date else "N/A"

    def __str__(self):
        return f"Project #{self.id}: {self.title} (Owner: {self.user_name})"