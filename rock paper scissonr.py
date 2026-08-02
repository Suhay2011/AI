import random

choices = ["rock", "paper", "scissors"]

print("=== Rock, Paper, Scissors ===")
print("Choose: rock, paper, or scissors")

# Get user's choice
user_choice = input("Your choice: ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid choice! Please run the program again and choose rock, paper, or scissors.")
else:
    print("\nYou chose:", user_choice)

    ai_choice = random.choice(choices)

    print("AI is choosing...")
    print("AI chose:", ai_choice)

    if user_choice == ai_choice:
        print("\nIt's a tie!")
    elif (
        (user_choice == "rock" and ai_choice == "scissors") or
        (user_choice == "paper" and ai_choice == "rock") or
        (user_choice == "scissors" and ai_choice == "paper")
    ):
        print("\n🎉 You win!")
    else:
        print("\n🤖 AI wins!")

print("\nThanks for playing!")
