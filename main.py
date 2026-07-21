from models.user import User
from models.project import Project
from models.task import Task

def display_menu():
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
    memory = {
        "users": [],
        "projects": [],
        "tasks": []
    }

    while True:
        display_menu()
        choice = input("Enter a choice (1-8): ").strip()

        if choice == "1":
            print("\n--- Add New User ---")
            name = input("Enter user name: ").strip()
            email = input("Enter user email: ").strip()

            if name and email:
                user = User(name, email)
                memory["users"].append(user)
                print(f"Added: {user}")
            else:
                print("Name and email cannot be empty.")

        elif choice == "2":
            print("\n=== USERS ===")
            if not memory["users"]:
                print("No users found.")
            else:
                for u in memory["users"]:
                    print(u)

        elif choice == "3":
            print("\n--- Add New Project ---")
            user_name = input("Enter owner's user name: ").strip()

            user_exists = False
            for u in memory["users"]:
                if u.name.lower() == user_name.lower():
                    user_exists = True
                    break

            if not user_exists:
                print(f"Error: User '{user_name}' does not exist. Please create the user first.")
                continue

            title = input("Enter project title: ").strip()
            description = input("Enter description (optional): ").strip()
            due_date = input("Enter due date e.g. 2026-12-31 (optional): ").strip()

            if title:
                project = Project(title, user_name, description, due_date)
                memory["projects"].append(project)
                print(f"Created: {project}")
            else:
                print("Project title cannot be empty.")

        elif choice == "4":
            print("\n=== PROJECTS ===")
            if not memory["projects"]:
                print("No projects found.")
            else:
                for p in memory["projects"]:
                    print(p)

        elif choice == "5":
            print("\n--- Add Task to Project ---")
            project_title = input("Enter project title: ").strip()

            proj_exists = False
            for p in memory["projects"]:
                if p.title.lower() == project_title.lower():
                    proj_exists = True
                    break

            if not proj_exists:
                print(f"Error: Project '{project_title}' does not exist.")
                continue

            task_title = input("Enter task title: ").strip()
            assignee = input("Enter assignee name (optional): ").strip()

            if task_title:
                task = Task(task_title, project_title, assigned_to=assignee)
                memory["tasks"].append(task)
                print(f"Created: {task}")
            else:
                print("Task title cannot be empty.")

        elif choice == "6":
            print("\n=== TASKS ===")
            if not memory["tasks"]:
                print("No tasks found.")
            else:
                for t in memory["tasks"]:
                    print(t)

        elif choice == "7":
            print("\n--- Complete a Task ---")
            task_id_input = input("Enter Task ID to mark completed: ").strip()

            if task_id_input.isdigit():
                task_id = int(task_id_input)
                task_found = False

                for t in memory["tasks"]:
                    if t.id == task_id:
                        t.status = "Completed"
                        task_found = True
                        break

                if task_found:
                    print(f"Task #{task_id} marked as Completed.")
                else:
                    print(f"Error: Task #{task_id} not found.")
            else:
                print("Please enter a valid numerical Task ID.")

        elif choice == "8":
            print("\nGoodbye! Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()