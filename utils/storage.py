import json
import os
import logging
from models.user import User
from models.project import Project
from models.task import Task

logging.basicConfig(
    filename="app.log", 
    level=logging.ERROR
    )

DATA_FILE = os.path.join("data", "database.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": [], "tasks": []}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            users = [User.from_dict(u) for u in data.get("users", [])]
            projects = [Project.from_dict(p) for p in data.get("projects", [])]
            tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
            return {"users": users, "projects": projects, "tasks": tasks}
            
    except (json.JSONDecodeError, Exception) as error:
        logging.error(f"Error loading data file: {error}")
        print("Warning: Could not read database file. Starting fresh.")
        return {"users": [], "projects": [], "tasks": []}

def save_data(db):
    """Converts objects to dictionaries and saves to JSON file."""
    try:
        os.makedirs("data", exist_ok=True)
        serialized_data = {
            "users": [u.to_dict() for u in db["users"]],
            "projects": [p.to_dict() for p in db["projects"]],
            "tasks": [t.to_dict() for t in db["tasks"]]
        }
        with open(DATA_FILE, "w") as file:
            json.dump(serialized_data, file, indent=4)
    except Exception as error:
        logging.error(f"Error saving data: {error}")
        print(f"Error saving data to disk: {error}")