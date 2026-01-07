def main():
    print("Welcome to CLI to-do List manager Softower.")
    fetures()
    choice = int(input("Enter your choice: "))

    match choice:
        case 1: addTask()
        case 2: removeTask()
        case _: print("This isn't valid option")
    

def fetures():
    print("What doy want to do?"); print()
    print("1. Add Task.")
    print("2. Remove Task.")
    print("--------------------------------")

def addTask():
    print("Hey task added")

def removeTask():
    print("Hey task removed")

main()