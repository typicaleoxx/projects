import random

emoji_languages = {
    "🐍": "python",
    "🌐": "javascript",
    "☕": "java",
    "💻": "c++",
    "💎": "ruby",
    "📄": "html",
    "🎨": "css",
    "🐘": "php",
    "🍏": "swift",
    "🔒": "c#",
    "🚀": "go",
}


def main():
    user_ready = input("Are you ready for a fun round? (yes/no)").lower()
    try:
        if user_ready == "yes" or user_ready == "no":
            if user_ready == "yes":
                game()
            else:
                print("Okay, have a great time ahead.")
    except:
        print("Invalid choice. Try again")


def game():
    score = 0
    for i in range(5):
        list_emoji_languages = list(emoji_languages.keys())
        game_guess = random.choice(list_emoji_languages)
        user_guess = input(f"Guess language({game_guess}): ").lower()
        if emoji_languages.get(game_guess) == user_guess:
            print("Congratulations. You guessed it right.")
            score += 1
        else:
            print(f"Oops, wrong guess. It's {emoji_languages.get(game_guess)}.")
    total_score(score)


def total_score(score):
    print(f"Congratulations! You scored {score} out of 5")
    ask = input("Do you want to play again? (yes/no)").lower()
    try:
        if ask == "yes" or ask == "no":
            if ask == "yes":
                game()
            elif ask == "no":
                print("It was nice seeing you. Have a great day ahead.")
    except:
        print("Oops, wrong input. Try again.")


main()
