import csv

def main():
    print("Welcome to CLI to-do List manager Softower.")
    fetures()
    choice = int(input("Enter your choice: "))

    match choice:
        case 1: addTask()
        case 2: viewtask_byNumber()
        case 3: view_All_Tasks()
        case 4: editTask()
        case 5: removeTask()
        case _: print("This isn't valid option")    

def fetures():
    print("What doy want to do?"); print()
    print("1. Add Task.")
    print("2. view your Task By Serial.")
    print("3. view All Tasks.")
    print("4. Edits Task.")
    print("5. Remove Task.")
    print("--------------------------------")

def addTask():
    print("You have to write these to add Task")
    task_name = input("1.Task Name: ")
    task_number = int(input("2.Task Number: "))
    task_setailes = input("3.Detailes (up to 20 char): ")
    task_Due = input("4.Due: ")

    with open("tasks.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([task_number,task_name, task_setailes, task_Due])
    print(f"{task_name} added successfully as Task.")    

def viewtask_byNumber():
    found = False
    task_number = input("Enter the task number: ")  
    with open("tasks.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["task_Number"] == task_number:
                print("\nTask Found:\n")
                print(f"Priority   : {row['task_Number']}")
                print(f"Task       : {row['task_name']}")
                print(f"Details    : {row['task_detailes']}")
                print(f"Time to do : {row['task_due']}")
                found = True
                break
        else: print("Not Found!")            



def view_All_Tasks():
    print("Hey these are your task")    

def editTask():
    print("Your Task Edited")

def removeTask():
    print("Hey task removed")


main()