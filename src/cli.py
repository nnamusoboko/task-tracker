import argparse

def creat_arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="task-cli", description="Task Tracker CLI")
    sub_parsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = sub_parsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="description of the task")

    update_parser = sub_parsers.add_parser("update", help="update a task")
    task_id_parser = update_parser.add_parser("task_id", help="id of the task to update")
    task_id_parser.add_argument("description", type=str, help="data to update with")

    delete_parser = sub_parsers.add_parser("delete", help="delete a task")
    delete_parser.add_argument("task_id", type=int, help="id of task to delete")

    mark_in_progress_parser = sub_parsers.add_parser("mark_in_progress", help="mark task in progress")
    mark_in_progress_parser.add_argument("task_id", type=int, help="id of task to mark as in progress")

    mark_done_parser = sub_parsers.add_parser("mark_done", help="mark a task as done")
    mark_done_parser.add_argument("task_id", type=int, help="id of task to mark as done")

    list_parser = sub_parsers.add_parser("list", help="list all tasks")
    list_parser.add_argument(
        "status",
        type=str,
        nargs="?",
        choices=["done", "todo", "in-progress"]
    )

    return parser.parse_args()
