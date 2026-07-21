from main import build_parser

def test_add_user_parser():
    parser = build_parser()
    args = parser.parse_args(["add-user", "--name", "Alex", "--email", "alex@test.com"])
    assert args.command == "add-user"
    assert args.name == "Alex"
    assert args.email == "alex@test.com"

def test_complete_task_parser():
    parser = build_parser()
    args = parser.parse_args(["complete-task", "--id", "1"])
    assert args.command == "complete-task"
    assert args.id == 1