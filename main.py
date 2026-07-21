import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data
from utils.formatting import print_table

def build_parser():
    """Builds and configures the argparse subcommands."""
    parser = argparse.ArgumentParser(description="Admin CLI Project Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Command: add-user
    user_parser = subparsers.add_parser("add-user", help="Add a new user")
    user_parser.add_argument("--name", required=True, help="User name")
    user_parser.add_argument("--email", required=True, help="User email")

    # Command: list-users
    subparsers.add_parser("list-users", help="List all users")

    # Command: add-project
    project_parser = subparsers.add_parser("add-project", help="Add a new project")
    project_parser.add_argument("--user", required=True, help="Owner user name")
    project_parser.add_argument("--title", required=True, help="Project title")
    project_parser.add_argument("--description", default="", help="Project description")
    project_parser.add_argument("--due", default="N/A", help="Due date")

    # Command: list-projects
    subparsers.add_parser("list-projects", help="List all projects")

    # Command: add-task
    task_parser = subparsers.add_parser("add-task", help="Add a task to a project")
    task_parser.add_argument("--project", required=True, help="Parent project title")
    task_parser.add_argument("--title", required=True, help="Task title")
    task_parser.add_argument("--assignee", default=None, help="Assigned user name")

    # Command: complete-task
    complete_parser = subparsers.add_parser("complete-task", help="Mark a task completed")
    complete_parser.add_argument("--id", type=int, required=True, help="Task ID")

    # Command: list-tasks
    subparsers.add_parser("list-tasks", help="List all tasks")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    # Load persistent data
    db = load_data()

    # --- COMMAND ROUTING ---
    if args.command == "add-user":
        user = User(args.name, args.email)
        db["users"].append(user)
        save_data(db)
        print(f"✅ Added {user}")

    elif args.command == "list-users":
        rows = [[u.id, u.name, u.email] for u in db["users"]]
        print_table(rows, ["ID", "Name", "Email"], "USERS")

    elif args.command == "add-project":
        # Check user exists
        user_exists = any(u.name.lower() == args.user.lower() for u in db["users"])
        if not user_exists:
            print(f"❌ Error: User '{args.user}' does not exist.")
            return

        project = Project(args.title, args.user, args.description, args.due)
        db["projects"].append(project)
        save_data(db)
        print(f"✅ Created {project}")

    elif args.command == "list-projects":
        rows = [[p.id, p.title, p.user_name, p.due_date, p.description] for p in db["projects"]]
        print_table(rows, ["ID", "Title", "Owner", "Due Date", "Description"], "PROJECTS")

    elif args.command == "add-task":
        # Check project exists
        proj_exists = any(p.title.lower() == args.project.lower() for p in db["projects"])
        if not proj_exists:
            print(f"❌ Error: Project '{args.project}' does not exist.")
            return

        task = Task(args.title, args.project, assigned_to=args.assignee)
        db["tasks"].append(task)
        save_data(db)
        print(f"✅ Created {task}")

    elif args.command == "complete-task":
        task_found = False
        for t in db["tasks"]:
            if t.id == args.id:
                t.status = "Completed"
                task_found = True
                break

        if task_found:
            save_data(db)
            print(f"✅ Task #{args.id} marked as Completed.")
        else:
            print(f"❌ Error: Task #{args.id} not found.")

    elif args.command == "list-tasks":
        rows = [[t.id, t.title, t.project_title, t.status, t.assigned_to or "Unassigned"] for t in db["tasks"]]
        print_table(rows, ["ID", "Title", "Project", "Status", "Assignee"], "TASKS")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()