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
    elif user_choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
main()