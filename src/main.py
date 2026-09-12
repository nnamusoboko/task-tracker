from src.cli import create_arg_parser

def main():
    args = create_arg_parser()
    command = args.command

    match command:
        case "add":
            print(f"[{args.description}] will be added to tasks")

if __name__ == "__main__":
    main()
