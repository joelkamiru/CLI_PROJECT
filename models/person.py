# models/person.py

class Person:

    def __init__(self, name, email):
        self.name = name
        self._email = ""
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        val_str = str(value).strip() if value else ""

        if "@" in val_str:
            self._email = val_str
        else:
            print("\n Warning: Invalid email format! Defaulting to 'unknown@example.com'.")
            self._email = "unknown@example.com"

    def __str__(self):
        return f"{self.name} ({self.email})"