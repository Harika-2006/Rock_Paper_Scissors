import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    while True:
        user = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if user == "quit":
            print("Thanks for playing!")
            break
        if user not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.")
            continue

        computer = get_computer_choice()
        print(f"🤖 Computer chose: {computer}")
        result = get_winner(user, computer)
        print(f"📢 {result}\n")

if __name__ == "__main__":
    main()
