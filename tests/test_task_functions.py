from datetime import datetime
import json
from pathlib import Path

import pytest

from src.task_functions import (
    Task,
    TaskStatus,
    add_task,
    build_new_task,
    format_task_list,
    save_tasks
)


def make_task(task_id: int, description: str, status: TaskStatus) -> Task:
    now = datetime.now().isoformat()
    return {
        "id": task_id,
        "description":description,
        "status": status,
        "createdAt": now,
        "updatedAt": now
    }

def test_build_new_task_assigns_unique_ids():
    task1 = build_new_task("go to hackathon", [], datetime.now().isoformat())
    task2 = build_new_task("come back from hackathon", [task1], datetime.now().isoformat())

    assert task1["id"] == 1
    assert task2["id"] == 2

def test_add_task_to_empty_list():
    task: Task = make_task(1, "code tonight", "todo")

    tasks = add_task(task, [])
    assert len(tasks) == 1
    assert tasks[0]["description"] == "code tonight"

def test_add_task_rejects_duplicate_id():
    existing = make_task(4, "snipe tokens", "done")
    duplicate_task: Task = {**existing, "description": "go to gym"} # type: ignore[typeddict-item]

    with pytest.raises(ValueError):
        add_task(duplicate_task, [existing])

def test_add_task_accepts_duplicate_task_descriptions():
    task1 = make_task(1, "go to hackathon", "todo")
    task2 = make_task(2, "go to hackathon", "in-progress")

    tasks = add_task(task1, [])
    tasks = add_task(task2, tasks)

    assert len(tasks) == 2
    assert tasks[0]["description"] == tasks[1]["description"]


def test_format_task_list():
    empty_list_default_str = format_task_list([])
    task: Task = make_task(1, "code tonight", "todo")
    formatted_tasks_str = format_task_list([task])

    assert empty_list_default_str == "No tasks added yet"
    assert formatted_tasks_str == f"Tasks: \n{task['id']}. {task['description']}  status: {task['status']}"

def test_save_tasks(tmp_path: Path):
    file_path = tmp_path / "tasks.json"

    task1 = make_task(2, "go to hackathon", "in-progress")

    save_tasks([task1], file_path)

    assert file_path.exists()

    written_data = json.loads(file_path.read_text())
    assert written_data == [task1]
