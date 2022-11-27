from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, start_text, shift_amount):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            position = letter_index + shift_amount
            end_text += alphabet[position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}\n")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(direction, text, shift)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if answer == "no":
        print("Goodbye")
        break