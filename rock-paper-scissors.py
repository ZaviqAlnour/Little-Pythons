import random

valid_choices = ["rock", "paper", "scissors"]

name = input("Enter your name: ")
print(f"\nHey, welcome back {name}!")
print("---------------------------")
print("This is the Rock, Paper & Scissors game.")
print()

round_choice = int(input("How many rounds do you want to play?: "))

print("\nRules:")
print("Rock win  -> +2 points")
print("Paper win -> +1 point")
print("Scissors win -> +3 points")
print("\nType 'q' anytime to quit the game.")
print("------------------------------------------")

user_point = 0
computer_point = 0

for round_no in range(1, round_choice + 1):

    print(f"\nRound {round_no}")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice == "q":
        print("\nYou quit the game early.")
        break

    if user_choice not in valid_choices:
        print("Invalid input. Please type one of these correctly:")
        print(valid_choices)
        continue

    computer_choice = random.randint(1, 3)

    match (computer_choice, user_choice):

        case (1, "rock"):
            user_point += 2
            computer_point += 2
            print("Draw! Both players got +2 points.")

        case (2, "paper"):
            user_point += 1
            computer_point += 1
            print("Draw! Both players got +1 point.")

        case (3, "scissors"):
            user_point += 3
            computer_point += 3
            print("Draw! Both players got +3 points.")

        case (1, "paper"):
            user_point += 1
            print("You won this round! You got +1 point.")

        case (2, "scissors"):
            user_point += 3
            print("You won this round! You got +3 points.")

        case (3, "rock"):
            user_point += 2
            print("You won this round! You got +2 points.")

        case (1, "scissors"):
            computer_point += 2
            print("Computer won this round! Computer got +2 points.")

        case (2, "rock"):
            computer_point += 1
            print("Computer won this round! Computer got +1 point.")

        case (3, "paper"):
            computer_point += 3
            print("Computer won this round! Computer got +3 points.")

print("\n---------- GAME OVER ----------")
print(f"Your total points: {user_point}")
print(f"Computer total points: {computer_point}")

if user_point > computer_point:
    print(f"Congratulations {name}, you won the game!")
elif user_point < computer_point:
    print(f"Sorry {name}, you lost the game.")
else:
    print("The game ended in a draw.")

print("\nThank you for playing!")
print("Goodbye!")
