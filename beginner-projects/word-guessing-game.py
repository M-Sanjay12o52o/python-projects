import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'building',
         'swimming', 'skieing', 'dracula', 'miner', 'bitcoin',
         'crypto', 'poker', 'politics', 'minion', 'market',
         'maths', 'science', 'magic', 'glow', 'armour', 'artist',
         'rupee', 'dollar', 'coin', 'circus', 'elephant', 'tiger',
         'lion', 'rambo']

# Select a random word
# word = random.choice(words)
word = "banana"
display_word = ["_"] * len(word)
chances = 6
chances_count = 0

letter_positions = {}

for index, letter in enumerate(word):
  if letter in letter_positions:
    letter_positions[letter].append(index)
  else:
    letter_positions[letter] = [index]

revealed_count = {letter: 0 for letter in word}

print("Initial revealed_count: ", revealed_count)

while "_" in display_word and chances_count < chances:
  chances_left = chances - chances_count
  print(f"Chances left: {chances_left}")
  print(f"The word you are trying to guess has {len(word)} characters.")
  print("Current word: ", " ".join(display_word))

  user_input_char = input(f"Please Enter your Guess Char: ")

  if user_input_char in letter_positions:
    if revealed_count[user_input_char] < len(letter_positions[user_input_char]):
      print(revealed_count[user_input_char] < len(letter_positions[user_input_char]))
      pos_to_reveal = letter_positions[user_input_char][revealed_count[user_input_char]]
      print("pos_to_reveal:", pos_to_reveal)
      display_word[pos_to_reveal] = user_input_char
      revealed_count[user_input_char] += 1
    else:
      print(f"All occurences of '{user_input_char}' have already been revealed.")
  else:
    chances_count += 1
    print(f"'{user_input_char}' is not in the word")

print("\nFinal word:", " ".join(display_word))
if "_" not in display_word:
  print("Congratulations! You've revealed the whole word.")
else:
  print("Game Over! You've run out of chances.")
  print("The word was:", word)