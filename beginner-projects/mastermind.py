import random

# Generates a number between 1000 and 9999
number = str(random.randint(1000, 9999))
random_number = [digit for digit in number]

display_number = ["_"] * len(random_number)
chances = 6
chances_count = 0

number_positions = {}

for index, number in enumerate(random_number):
  if number in number_positions:
    number_positions[number].append(index)
  else:
    number_positions[number] = [index]

revealed_count = {number: 0 for number in random_number}

while "_" in display_number:
  chances_left = chances - chances_count
  print(f"Chances left: {chances_left}")
  print("Current number: ", " ".join(display_number))
  user_guess_number = str(input(f"Please input your guess number: "))

  if user_guess_number in number_positions:
    if revealed_count[user_guess_number] < len(number_positions[user_guess_number]):
      pos_to_reveal = number_positions[user_guess_number][revealed_count[user_guess_number]]
      display_number[pos_to_reveal] = user_guess_number
      revealed_count[user_guess_number] += 1
    else:
      print(f"All occurences of '{user_guess_number}' have already been revealed.")
  else:
    chances_count += 1
    print(f"'{user_guess_number}' is not in the selected number.")

print("\nFinal complete number:", " ".join(display_number))
if "_" not in display_number:
  print("Congratulations! You've revealed the whole word.")
else:
  print("Game Over! You've run out of chances.")
  print("The word was:", random_number)