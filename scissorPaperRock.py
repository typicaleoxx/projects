import random
actions = ["scissors", "paper", "rock" ]

def main():
    user_choice = input("Enter your choice (scissors, paper, rock): ")
    game(user_choice)
    
def game(user_choice):
    computer_action = random.choice(actions)
    print(f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

    if user_choice == computer_action:
        print(f"Both players selected {user_choice}. It's a tie!")
        again()
    elif user_choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            again()
        else:
            print("Paper covers rock! You lose.")
            again()
    elif user_choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            again()
        else:
            print("Scissors cuts paper! You lose.")
            again()
    elif user_choice == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            again()
        else:
            print("Rock smashes scissors! You lose.")
            again()

def again():
    ask=input("Do you want to play again? (y/n)").strip().lower()
    if ask=="y":
        main()
    else:
        print("Have a great day.")
main()