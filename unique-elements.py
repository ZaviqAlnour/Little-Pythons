arrayOfUniqueNum = []

while True:
    try:
        element = int(input("Enter a unique number: "))
        if element in arrayOfUniqueNum:
            print("This number already exists!")
        else:
            arrayOfUniqueNum.append(element)
            print(f"Added {element} to the list.")
        
        choixe = input("Do you want to add more? (y/n): ").lower()
        if choixe != "y":
            break

    except ValueError:
        print("That's not a valid number!")
        choixe = input("Do you want to try again? (y/n): ").lower()
        if choixe != "y":
            break

print("Final list of unique numbers:", arrayOfUniqueNum)
