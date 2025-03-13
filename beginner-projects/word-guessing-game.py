import random

# name = input("What is your name? ")
# print(f"Hi, {name}, Welcome to the Word guessing game. Here you need to guess the random word that we have selected for you. With ONE Character at a time.")
# print(input("Press ENTER to continue."))

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'building',
         'swimming', 'skieing', 'dracula', 'miner', 'bitcoin',
         'crypto', 'poker', 'politics', 'minion', 'market',
         'maths', 'science', 'magic', 'glow', 'armour', 'artist',
         'rupee', 'dollar', 'coin', 'circus', 'elephant', 'tiger',
         'lion', 'rambo']

# word = random.choice(words)
word = "banana"

print("Word to be guessed:", word)

number_of_attempts = 12
count_attempts = 0
result = []
copy_word = word

for n in range(len(word)):
      result.append("_")

while count_attempts < 12:
  attempts_left = number_of_attempts - count_attempts - 1

  if count_attempts == 0:
    print(f"The word you are trying to guess has {len(word)} characters.")

  if "_" not in result:
    print(f"Congrats! You have won the game. In {count_attempts} attempts.")
    break

  user_input_char = input("Please input your character here: ")

  if list(dict.fromkeys(word)):
    print("duplicate char's: ", word) 

  if user_input_char in word and len(user_input_char) == 1: 
    if type(user_input_char) == int:
      print("Int input is not valid. Kindly input a character.") 
    result[word.index(user_input_char)] = user_input_char
    copy_word.replace(user_input_char, "_")
    for n in result:
      print(n)
  elif len(user_input_char) > 1:
    print("Characters should only be of length 1.")
  elif user_input_char not in word:
    count_attempts += 1
    print("That particular character is not in the word. Please try again.")
    print(f"You have {attempts_left} attempts left.")



