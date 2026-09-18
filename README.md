# Task tracker

A simple cli based task tracker

## actions 

### Adding a new task

```bash
task-cli add "Buy groceries"
```

### Updating and deleting tasks

```bash
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

### Marking a task as in progress or done

```bash
task-cli mark-in-progress 1
task-cli mark-done 1
```

### Listing all tasks

```bash 
task-cli list
```

### Listing tasks by status

```bash
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Get started

1. **clone repo**
```bash
git clone https://github.com/nnamusoboko/task-tracker
cd task-tracker
```

2. **set up environment**
```bash
uv sync
```
