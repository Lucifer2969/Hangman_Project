import random
from Hangman_art import stages, logo
from Hangman_word import word_list

word = random.choice(word_list)
placeholder = ""
lives = 5
game_over = False
print(logo)
print(word)
word_length = len(word)
correct_word = []
for position in range(word_length):
    placeholder += '_'
print(placeholder)
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
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
    if guess not in word:
        print("You have guessed wrong letter. Lives will be reduced")
        lives -= 1
        print("*****Lives left is:-",lives,"*****")
        if lives == 0:
            print("You loose")
            game_over = True
    if '_' not in display:
        game_over = True
        print("You win!")
    print(stages[lives])