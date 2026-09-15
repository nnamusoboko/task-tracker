from src.cli import create_arg_parser
from src.task_functions import CommandPayload, execute_command


def main():
    args = create_arg_parser()
    command = args.command

    match command:
        case "add":
            execute_command({
                "command": command,
                "description": args.description
            })
        case "list":
            execute_command({
                "command": command
            })
        case "update":
            execute_command({
                "command": command,
                "description": args.description,
                "id": args.task_id
            })
        case "delete":
            execute_command({
                "command": command,
                "id": args.task_id
            })



if __name__ == "__main__":
    main()
