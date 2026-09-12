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

class BaseTask(TypedDict):
    id: int
    description: str
    status: TaskStatus
    created_at: str

class NewTask(BaseTask):
    pass

class UpdatedTask(BaseTask):
    update_at: str

class JsonFileData(TypedDict):
    tasks: list[NewTask|UpdatedTask]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FILE_PATH = PROJECT_ROOT / "data" / "tasks.json"
FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

def execute_command(command: CommandPayload):
    if command['command'] == "add":
        if "description" not in command:
            print("Provide a description")
            return

        task: NewTask = {
            "id": 1,
            "description": command["description"],
            "status": "todo",
            "created_at": datetime.now().isoformat()
        }

        add_task(task)
        return
    if command['command'] == "delete":
        return
    if command['command'] == "update":
        return
    if command['command'] == "list":
        list_tasks()
        return


def add_task(task: NewTask) -> None:
    tasks = load_tasks(FILE_PATH)

    for stored_task in tasks:
       if task["id"] == stored_task["id"]:
           print(f"[{task['description']}] already exists")
           return
    tasks.append(task)

    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"[{task['description']}] added to tasks")

def list_tasks() -> None:
     tasks = load_tasks(FILE_PATH)

     if not tasks:
         print("No tasks added yet")
         return

     print("Tasks: ")
     for index, task in enumerate(tasks):
         print(f"{index+1}. {task['description']}  status: {task['status']}")


def load_tasks(path: Path) -> list[NewTask | UpdatedTask]:
    tasks: list[NewTask|UpdatedTask] = []
    if path.exists():
        with open(path, "r") as f:
            try:
                tasks = json.load(f)
            except JSONDecodeError:
                tasks = []
    return tasks
