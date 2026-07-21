# models/user.py

from models.person import Person

class User(Person):
    
    id_counter = 1

    def __init__(self, name, email, user_id=None):
        super().__init__(name, email)
        
        if user_id is not None:
            self.id = int(user_id)
            if self.id >= User.id_counter:
                User.id_counter = self.id + 1
        else:
            self.id = User.id_counter
            User.id_counter += 1

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], email=data["email"], user_id=data.get("id"))

    def __str__(self):
        return f"User #{self.id}: {self.name} - {self.email}"