from datetime import datetime

import pytest

from src.task_functions import Task, add_task, build_new_task, format_task_list


def test_add_task_to_empty_list():
    now = datetime.now().isoformat()
    task: Task = build_new_task("code tonight", [], now)

    tasks = add_task(task, [])
    assert len(tasks) == 1
    assert tasks[0]["description"] == "code tonight"

def test_add_task_rejects_duplicate_id():
    now  = datetime.now().isoformat()
    existing = build_new_task("snipe tokens", [], now)
    duplicate_task: Task = {**existing, "description": "go to gym"} # type: ignore[typeddict-item]

    with pytest.raises(ValueError):
        add_task(duplicate_task, [existing])

def test_add_task_accepts_duplicate_task_descriptions():
    task1 = build_new_task("go to hackathon", [], datetime.now().isoformat())
    task2 = build_new_task("go to hackathon", [task1], datetime.now().isoformat())

    tasks = add_task(task1, [])
    tasks = add_task(task2, tasks)

    assert len(tasks) == 2
    assert tasks[0]["description"] == tasks[1]["description"]

def test_build_new_task_assigns_unique_ids():
    task1 = build_new_task("go to hackathon", [], datetime.now().isoformat())
    task2 = build_new_task("come back from hackathon", [task1], datetime.now().isoformat())

    assert task1["id"] == 1
    assert task2["id"] == 2

def test_format_task_list():
    empty_list_default_str = format_task_list([])
    now =  datetime.now().isoformat()
    task: Task = {
        "id":1, "description":
        "Code tonight",
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks_str = format_task_list([task])

    assert empty_list_default_str == "No tasks added yet"
    assert tasks_str == f"Tasks: \n{task['id']}. {task['description']}  status: {task['status']}"
