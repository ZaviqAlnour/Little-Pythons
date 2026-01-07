import random

name = input("Name: ")
print(f"Hey welcome Back! {name}")
print("---------------------------")
print("This is the Rock, Paper & Scissors game buddy.")
round_choice = int(input("How many Round do you want to play?: "))
print("You just have to right rock paper scissors.")
print("points----Bellw-----")
print()
print("1.if you got Rock and win the round your point will increase by = 2")
print("1.if you got Paper and win the round your point will increase by = 1")
print("3.if you got Scissors and win the round your point will increase by = 3")

user_choice = input("Enter your choice: ").lower()
computer_choice = random.randint(1, 3)

match (computer_choice, user_choice):
    case (1, "rock"):
        user_point, computer_point = 2, 2
        print("This is a draw. Both of you got +2")

    case (2, "paper"):
        user_point, computer_point = 1, 1
        print("This is a draw. Both of you got +1")

    case (3, "scissors"):
        user_point, computer_point = 3, 3
        print("This is a draw. Both of you got +3")

    case (1, "paper"): 
        user_point, computer_point = 1, 0
        print(f"Hey {name}, you won! You got +1")

    case (2, "scissors"): 
        user_point, computer_point = 3, 0
        print(f"Hey {name}, you won! You got +3")

    case (3, "rock"):  
        user_point, computer_point = 2, 0
        print(f"Hey {name}, you won! You got +2")

    case (1, "scissors"):
        user_point, computer_point = 0, 2
        print("Computer wins! Computer got +2")

    case (2, "rock"):
        user_point, computer_point = 0, 1
        print("Computer wins! Computer got +1")

    case (3, "paper"):
        user_point, computer_point = 0, 3
        print("Computer wins! Computer got +3")

    case _:
        print("Invalid input. Please choose rock, paper, or scissors.")
    