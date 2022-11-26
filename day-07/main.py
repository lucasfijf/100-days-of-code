import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_game = False

lives = 6

print(logo)
print(f"Pssst, the solution is {chosen_word}")

display = ["_" for letter in chosen_word]


print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win.")
    
    print(stages[lives])