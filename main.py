# main.py

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data
from utils.formatting import print_table

def display_menu():
    """Prints the main interactive options menu."""
    print("\n=================================")
    print("   ADMIN PROJECT MANAGER CLI     ")
    print("=================================")
    print("1. Add new user")
    print("2. List all users")
    print("3. Add new project")
    print("4. List all projects")
    print("5. Add task to a project")
    print("6. List all tasks")
    print("7. Complete a task")
    print("8. Exit")
    print("=================================")

def main():
    db = load_data()

    while True:
        display_menu()
        choice = input("Enter a choice (1-8): ").strip()

        if choice == "1":
            print("\n--- Add New User ---")
            name = input("Enter user name: ").strip()
            email = input("Enter user email: ").strip()

            if name and email:
                user = User(name, email)
                db["users"].append(user)
                save_data(db)
                print(f"Added {user}")
            else:
                print(" Name and email cannot be empty!")

        elif choice == "2":
            rows = [[u.id, u.name, u.email] for u in db["users"]]
            print_table(rows, ["ID", "Name", "Email"], "USERS")

        elif choice == "3":
            print("\n--- Add New Project ---")
            user_name = input("Enter owner's user name: ").strip()

            user_exists = any(u.name.lower() == user_name.lower() for u in db["users"])
            if not user_exists:
                print(f" Error: User '{user_name}' does not exist. Please create the user first.")
                continue

            title = input("Enter project title: ").strip()
            description = input("Enter description (optional): ").strip()
            due_date = input("Enter due date e.g. 2026-12-31 (optional): ").strip()

            if not due_date:
                due_date = "N/A"

            if title:
                project = Project(title, user_name, description, due_date)
                db["projects"].append(project)
                save_data(db)
                print(f" Created {project}")
            else:
                print(" Project title cannot be empty!")

        elif choice == "4":
            rows = [[p.id, p.title, p.user_name, p.due_date, p.description] for p in db["projects"]]
            print_table(rows, ["ID", "Title", "Owner", "Due Date", "Description"], "PROJECTS")

        elif choice == "5":
            print("\n--- Add Task to Project ---")
            project_title = input("Enter project title: ").strip()

            proj_exists = any(p.title.lower() == project_title.lower() for p in db["projects"])
            if not proj_exists:
                print(f"Error: Project '{project_title}' does not exist.")
                continue

            task_title = input("Enter task title: ").strip()
            assignee = input("Enter assignee name (optional): ").strip()

            if task_title:
                task = Task(task_title, project_title, assigned_to=assignee)
                db["tasks"].append(task)
                save_data(db)
                print(f" Created {task}")
            else:
                print("Task title cannot be empty!")

        elif choice == "6":
            rows = [[t.id, t.title, t.project_title, t.status, t.assigned_to or "Unassigned"] for t in db["tasks"]]
            print_table(rows, ["ID", "Title", "Project", "Status", "Assignee"], "TASKS")

        elif choice == "7":
            print("\n--- Complete a Task ---")
            task_id_input = input("Enter Task ID to mark completed: ").strip()

            if task_id_input.isdigit():
                task_id = int(task_id_input)
                task_found = False

                for t in db["tasks"]:
                    if t.id == task_id:
                        t.status = "Completed"
                        task_found = True
                        break

                if task_found:
                    save_data(db)
                    print(f"Task #{task_id} marked as Completed.")
                else:
                    print(f"Error: Task #{task_id} not found.")
            else:
                print(" Please enter a valid numerical Task ID.")

        # CHOICE 8: Exit
        elif choice == "8":
            print("\nGoodbye! Saving data and exiting...")
            break

        else:
            print(" Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()