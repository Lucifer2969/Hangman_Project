import random
stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
     |
========
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
     |
========
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
     |
========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
     |
========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
     |
========
''','''
 +---+
 |   |
     |
     |
     |
     |
     |
========
''']
word_list = ["camel","baboon","aardvark"]
word = random.choice(word_list)
placeholder = ""
lives = 5
game_over = False
print(word)
word_length = len(word)
correct_word = []
for position in range(word_length):
    placeholder += '_'
print(placeholder)
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in word:
        for letter in word:
            if letter == guess:
                display += letter
                correct_word.append(letter)
            elif letter in correct_word:
                display += letter
            else:
                display += '_'
    else:
        display += '_'
        lives -= 1
    print(display)
    print(stages[lives])
    if lives == 0:
        print("You loose")
        break
    if '_' not in display:
        game_over = True
        print("You win!")