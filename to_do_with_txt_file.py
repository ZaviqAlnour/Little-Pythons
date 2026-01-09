import csv
import sys
import os


FILE_NAME = "tasks.csv"
FIELDNAMES = ["task_number", "task_name", "task_details", "task_due"]


def main():
    print("Welcome to the CLI To-Do List Manager Software.")
    print()
    features()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        sys.exit(1)

    match choice:
        case 1:
            add_task()
        case 2:
            view_task_by_number()
        case 3:
            view_all_tasks()
        case 4:
            edit_task()
        case 5:
            clear_tasks_list()
        case _:
            print("This is not a valid option.")


def features():
    print("What do you want to do?")
    print()
    print("1. Add a task.")
    print("2. View a task by number.")
    print("3. View all tasks.")
    print("4. Edit a task.")
    print("5. Clear all tasks.")
    print("--------------------------------")


def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_task():
    ensure_file_exists()

    print("Please enter the following details to add a task.")
    task_name = input("1. Task Name: ")
    task_number = input("2. Task Number: ")
    task_details = input("3. Details (up to 20 characters): ")
    task_due = input("4. Due Date / Time: ")

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(
            {
                "task_number": task_number,
                "task_name": task_name,
                "task_details": task_details,
                "task_due": task_due,
            }
        )

    print(f'Task "{task_name}" has been added successfully.')


def view_task_by_number():
    ensure_file_exists()

    task_number = input("Enter the task number: ")
    task_found = False

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["task_number"] == task_number:
                print()
                print("Task Found:")
                print("----------------------------")
                print(f"Task Number : {row['task_number']}")
                print(f"Task Name   : {row['task_name']}")
                print(f"Details     : {row['task_details']}")
                print(f"Due         : {row['task_due']}")
                task_found = True
                break

    if not task_found:
        print("Task not found.")


def view_all_tasks():
    ensure_file_exists()

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        tasks_exist = False

        for row in reader:
            tasks_exist = True
            print()
            print("----------------------------")
            print(f"Task Number : {row['task_number']}")
            print(f"Task Name   : {row['task_name']}")
            print(f"Details     : {row['task_details']}")
            print(f"Due         : {row['task_due']}")

        if not tasks_exist:
            print("No tasks available.")


def edit_task():
    ensure_file_exists()

    task_number_to_edit = input("Enter the task number you want to edit: ")
    task_found = False

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        tasks = list(reader)

    for task in tasks:
        if task["task_number"] == task_number_to_edit:
            print()
            print("Current Task Information:")
            print("----------------------------")
            print(f"Task Number : {task['task_number']}")
            print(f"Task Name   : {task['task_name']}")
            print(f"Details     : {task['task_details']}")
            print(f"Due         : {task['task_due']}")
            print()

            print("Enter new values (leave blank to keep the current value).")
            new_name = input("New Task Name: ")
            new_details = input("New Details: ")
            new_due = input("New Due Date / Time: ")

            if new_name:
                task["task_name"] = new_name
            if new_details:
                task["task_details"] = new_details
            if new_due:
                task["task_due"] = new_due

            task_found = True
            break

    if not task_found:
        print("Error: Task not found.")
        sys.exit(1)

    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

    print(f"Task {task_number_to_edit} has been updated successfully.")


def clear_tasks_list():
    ensure_file_exists()

    choice = input(
        "Do you really want to clear all tasks? Make sure all tasks are completed. (y/n): "
    ).lower()

    if choice in ["y", "yes"]:
        try:
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
            print("All tasks have been cleared successfully.")
        except IOError as error:
            print(f"Error clearing the task list: {error}")
    else:
        print("Operation cancelled.")


main()
