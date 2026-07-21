import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_user_creation():
    user = User("Alex", "alex@example.com")
    assert user.name == "Alex"
    assert user.email == "alex@example.com"

def test_task_status_setter():
    task = Task("Build CLI", "CLI Tool")
    assert task.status == "Pending"
    
    task.status = "Completed"
    assert task.status == "Completed"

def test_project_dictionary_conversion():
    proj = Project("CLI Tool", "Alex")
    data = proj.to_dict()
    
    recreated = Project.from_dict(data)
    assert recreated.title == "CLI Tool"
    assert recreated.user_name == "Alex"