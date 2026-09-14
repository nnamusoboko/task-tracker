import pytest
from src.cli import create_arg_parser

def test_add_command_parses_correctly():
    args = create_arg_parser(["add", "create super app"])

    assert args.command == "add"
    assert args.description == "create super app"

def test_update_command_parses_correctly():
    args = create_arg_parser(["update", "1", "code tonight"])

    assert args.command == "update"
    assert args.task_id == 1
    assert args.description == "code tonight"
    assert isinstance(args.task_id, int)

def  test_update_command_fails_without_task_id():
    with pytest.raises(SystemExit):
        create_arg_parser(["update", "code tonight"])

def  test_update_command_fails_without_description():
    with pytest.raises(SystemExit):
        create_arg_parser(["update", "1"])

def  test_update_command_fails_when_task_id_is_not_numeric():
    with pytest.raises(SystemExit):
        create_arg_parser(["update"])

def test_delete_command_parses_correctly():
    args = create_arg_parser(["delete", "4"])

    assert args.command == "delete"
    assert args.task_id == 4
    assert isinstance(args.task_id, int)

def  test_delete_command_fails_without_task_id():
    with pytest.raises(SystemExit):
        create_arg_parser(["delete"])

def test_list_with_no_status_command_parses_correctly():
    args = create_arg_parser(["list"])
    assert args.status is None

def test_list_with_status_command_parses_correctly():
    args = create_arg_parser(["list", "done"])

    assert args.status == "done"

def test_list_command_rejects_invalid_status():
    with pytest.raises(SystemExit):
     create_arg_parser(["list", "invalid-status"])

def test_mark_in_progress_parses_correctly():
    args = create_arg_parser(["mark_in_progress", "50"])

    assert args.command == "mark_in_progress"
    assert isinstance(args.task_id, int)

def test_mark_in_progress_command_fails_without_task_id():
    with pytest.raises(SystemExit):
        create_arg_parser(["mark_in_progress"])

def test_mark_done_parses_correctly():
    args = create_arg_parser(["mark_done",  "12"])

    assert args.command == "mark_done"
    assert isinstance(args.task_id, int)


def test_mark_done_command_fails_without_task_id():
    with pytest.raises(SystemExit):
        create_arg_parser(["mark_done"])
