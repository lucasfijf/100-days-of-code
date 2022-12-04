import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1, 100)
if level == "easy":
    lives = 10
elif level == "hard":
    lives = 5
while lives:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer as {number}.")
        break
    lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")