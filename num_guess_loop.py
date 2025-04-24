# Author: 2025 Mikhail Ibrahim
# Date: Apr 23, 2025
# Description: A crash-proof Python program that generates a random number
# between 1 and 10. The program uses a loop to keep asking the user to guess
# the number until they guess correctly. All invalid entries are handled
# to prevent the program from crashing.

import random

print("Welcome to the Number Guessing Game!")
print("Try to guess the number I'm thinking of between 1 and 10.")

# Generate the random correct number
correct_number = random.randint(1, 10)

# Loop until the user guesses correctly
while True:
    user_input = input("Enter your guess: ")

    try:
        guess = int(user_input)

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        if guess == correct_number:
            print(f"{guess}, You’ve guessed the random number correctly!")
            break
        else:
            print("Incorrect guess. Try again!")

    except ValueError:
        print(
            "Invalid input. Please enter digits only (no letters, symbols, or decimals)."
        )
