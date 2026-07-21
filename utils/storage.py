# utils/storage.py

import json
import os
from models.user import User
from models.project import Project
from models.task import Task

DATA_FILE = os.path.join("data", "database.json")


def load_data():
    """Loads stored JSON data and converts them back into objects."""
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": [], "tasks": []}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            users = [User.from_dict(u) for u in data.get("users", [])]
            projects = [Project.from_dict(p) for p in data.get("projects", [])]
            tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
            return {"users": users, "projects": projects, "tasks": tasks}
    except Exception as e:
        print(f" Notice: Starting with fresh data ({e})")
        return {"users": [], "projects": [], "tasks": []}


def save_data(db):
    try:
        os.makedirs("data", exist_ok=True)
        serialized_data = {
            "users": [u.to_dict() for u in db.get("users", [])],
            "projects": [p.to_dict() for p in db.get("projects", [])],
            "tasks": [t.to_dict() for t in db.get("tasks", [])],
        }
        with open(DATA_FILE, "w") as file:
            json.dump(serialized_data, file, indent=4)
    except Exception as error:
        print(f"\n Error saving data to disk: {error}")