from random import randint

rps = ["Rock", "Paper", "Scissors"]

answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

user = rps[answer]

random_number = randint(0, 2)

computer = rps[random_number]

if user == "Rock" and computer == "Scissors":
    result = "You win!"
elif user == "Scissors" and computer == "Paper":
    result = "You win!"
elif user == "Paper" and computer == "Rock":
    result = "You win!"
elif user == computer:
    result = "It's a tie!"
else:
    result = "You lose."

print(f"\n{user}")
print(f"\nComputer chose:\n\n{computer}")
print(f"\n{result}")