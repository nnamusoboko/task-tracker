import json
from datetime import datetime
from json.decoder import JSONDecodeError
from pathlib import Path
from typing import Literal, NotRequired, TypedDict

TaskStatus = Literal["todo", "in-progress", "done"]

class CommandPayload(TypedDict):
    command: str
    description: NotRequired[str]
    id: NotRequired[int]
    status: NotRequired[str]

class Task(TypedDict):
    id: int
    description: str
    status: TaskStatus
    createdAt: str
    updatedAt: str

class JsonFileData(TypedDict):
    tasks: list[Task]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FILE_PATH = PROJECT_ROOT / "data" / "tasks.json"
FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

def execute_command(command: CommandPayload):
    if command['command'] == "add":
        if "description" not in command:
            print("Provide a description")
            return
        try:
            saved_tasks = load_tasks(FILE_PATH)
            new_task = build_new_task(command["description"], saved_tasks, datetime.now().isoformat())
            updated_tasks = add_task(new_task, saved_tasks)

            save_tasks(updated_tasks, FILE_PATH)
            print(f"[{new_task['description']}] added to tasks")
            return
        except ValueError as err:
            print(f"Error: {err}")
    if command['command'] == "delete":
        return
    if command['command'] == "update":
        return
    if command['command'] == "list":
        list_tasks()
        return


def add_task(task: Task, tasks: list[Task]) -> list[Task]:
    if any(stored_task["id"] == task["id"] for stored_task in tasks):
        raise ValueError(f"Task with ID {task['id']} already exists.")
    return [*tasks, task]


def list_tasks() -> None:
     tasks = load_tasks(FILE_PATH)

     if not tasks:
         print("No tasks added yet")
         return

     print("Tasks: ")
     for index, task in enumerate(tasks):
         print(f"{index+1}. {task['description']}  status: {task['status']}")


def load_tasks(path: Path) -> list[Task]:
    tasks: list[Task] = []
    if path.exists():
        with open(path, "r") as f:
            try:
                tasks = json.load(f)
            except JSONDecodeError:
                tasks = []
    return tasks

def build_new_task(description: str, tasks: list[Task], current_date_string: str) -> Task:
    task_id = max((task["id"] for task in tasks), default=0) + 1
    return {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": current_date_string,
        "updatedAt": current_date_string
    }

def save_tasks(tasks: list[Task], file_path: Path) -> None:
    if file_path.exists():
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
