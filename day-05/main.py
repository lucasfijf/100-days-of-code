import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

arr = []

for x in range(num_letters):
    arr.append(random.choice(letters))

for x in range(num_symbols):
    arr.append(random.choice(symbols))

for x in range(num_numbers):
    arr.append(random.choice(numbers))

random.shuffle(arr)
password = "".join(arr)

print(f" Your password is: {password}")