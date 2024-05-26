import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["banana", "apple", "berries", "orange"]
#   choose a word randomly in the list
chosen_word = random.choice(word_list)
print(f"The word is: {chosen_word}")

#   set lives
lives = 6

#   create an empty list called display. for each letter in the chosen_word, add _ to display
display = []
for _ in chosen_word:
    display.append("_")
print(display)

#   loop through each position in the chosen_word
#   if the letter at that position matches 'guess'
#   then reveal that letter in the display at that position

end_of_game = False
while not end_of_game :
    #   guess a letter
    guess = input("Guess a letter: ").lower()

    #   check if the letter is one of the letters of the chosen word
    word_length = len(chosen_word)
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"current position: {position}\n current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    #   Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You won!")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Sorry, you lost!")
    print(stages[lives])


