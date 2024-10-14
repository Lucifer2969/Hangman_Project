import random
word_list = ["camel","baboon","aardvark"]
word = random.choice(word_list)
placeholder = ""
display = ""
print(word)
guess = input("Guess a letter: ").lower()
word_length = len(word)

for position in range(word_length):
    placeholder += '_'
print(placeholder)
for letter in word:
    if letter == guess:
        display += letter
    else:
        display += '_'
print(display)