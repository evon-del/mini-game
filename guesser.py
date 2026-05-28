import random

MIN_NUMBER  = 1    
MAX_NUMBER  = 100  
MAX_TRIES   = 7   

def play_game():
    """
    Runs one full round of the guessing game.
    Returns True if the player won, False if they ran out of tries.
    """

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    attempts = 0

    print("\n" + "=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print(f"  I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"  You have {MAX_TRIES} chances to guess it. Good luck!\n")

    while attempts < MAX_TRIES:

        tries_left = MAX_TRIES - attempts
        print(f"  Tries remaining: {tries_left}")

        raw_input_value = input("  Enter your guess: ").strip()

        if not raw_input_value.isdigit():
            print("  ⚠️  Invalid input! Please enter a whole number.\n")
            continue 

        guess = int(raw_input_value)

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"  ⚠️  Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.\n")
            continue  

        attempts += 1

        if guess < secret_number:
            print("Too low!  Try a higher number.\n")

        elif guess > secret_number:
            print("Too high! Try a lower number.\n")

        else:
            print("\n" + "=" * 50)
            print("  Congratulations! Your guess is correct.")
            print(f"  The secret number was {secret_number}.")
            print(f"  You found it in {attempts} attempt(s)!")
            print("=" * 50)
            return True   
    print("\n" + "=" * 50)
    print(f"  😞 Game over!  You've used all {MAX_TRIES} attempts.")
    print(f"  The secret number was {secret_number}.")
    print("=" * 50)
    return False   


def ask_play_again():
    """
    Asks the player whether they want to play another round.
    Keeps asking until the player enters Y or N (case-insensitive).
    Returns True to play again, False to quit.
    """
    while True:
        answer = input("\n  Would you like to play again? (Y/N): ").strip().upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Please enter Y for Yes or N for No.")

total_wins   = 0
total_losses = 0

while True:
    won = play_game()   

    if won:
        total_wins += 1
    else:
        total_losses += 1

    print(f"\n  📊 Score  →  Wins: {total_wins}  |  Losses: {total_losses}")

    if not ask_play_again():
        break

print("\n  Thanks for playing!  See you next time. 👋\n")