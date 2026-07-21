class Person:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in str(value):
            print("Warning: Invalid email address format.")
            self._email = "unknown@example.com"
        else:
            self._email = str(value)

    def __str__(self):
        return f"{self.name} ({self.email})"