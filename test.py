import os
import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        # Get user input
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            
            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
                
            attempts += 1
            
            # Check guess
            if guess == secret_number:
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            # Show remaining attempts
            print(f"You have {max_attempts - attempts} attempts left.")
            
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nGame Over! The number was {secret_number}.")
    print("Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()