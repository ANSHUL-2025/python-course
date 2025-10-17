import random

def guess_the_number():
    """
    A simple "Guess the Number" game in Python.
    The computer chooses a random number, and the user tries to guess it.
    """
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 7 attempts to guess it.")

    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return # End the game
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Game over! You ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()