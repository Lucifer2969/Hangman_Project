import random
from Hangman_art import stages, logo
from Hangman_word import word_list

# Generating random word from the word list.
word = random.choice(word_list)
placeholder = ""
lives = 5
game_over = False

# Using ASCII art to print logo.
print(logo)
# print(word)
word_length = len(word)
correct_word = []

# Generating Empty spaces based on the word length.
for position in range(word_length):
    placeholder += '_'
print(placeholder)

# While loop to check the termination condition and for loop to check correct letter in the word.
while not game_over:
    guess = input("Guess the correct letter: ").lower()
    display = ""
    print("*****Lives left is:-",lives,"*****")
    if guess in correct_word:
        print("You have already guessed",guess,"letter.")
    for letter in word:
        if letter == guess:
            display += letter
            correct_word.append(letter)
        elif letter in correct_word:
            display += letter
        else:
            display += '_'
    print(display)

# Conditional statement to check lives left for the user.
    if guess not in word:
        print("You have guessed wrong letter. Lives will be reduced")
        lives -= 1
        if lives == 0:
            print(f"You loose. Correct word is {word}")
            game_over = True

# Conditional statement to check if user has won the game.
    if '_' not in display:
        game_over = True
        print("You win!")
    print(stages[lives])