# Number guessing game in python

import random

print("Hi and Welcome to the Number Guessing game. You have 7 chances to guess a number between 1 to 100. Let's Play....")

list1 = range(1, 101)
number_of_choices = 7
count_of_choices = 0
number_to_guess = random.choice(list1)

while count_of_choices < number_of_choices:
  user_guess = int(input("Input your guess in the range of 1 to 100: "))
  balance_attempts = number_of_choices - count_of_choices - 1
  count_of_choices += 1

  if user_guess > number_to_guess:
    if count_of_choices == 7:
      print(f"Sorry, that was close. The number to be gussed was {number_to_guess}. Better Luck next time.")
    print(f"That was greater then the number to be guessed. You have {balance_attempts} attempts left")

  elif user_guess < number_to_guess:
    if count_of_choices == 7:
      print(f"Sorry, that was close. The number to be gussed was {number_to_guess}. Better Luck next time.")
    print(f"That was less then the number to be guessed. You have {balance_attempts} attempts left")  

  elif user_guess == number_to_guess:
    print(f"That was wonderful you've guessed it right. In {count_of_choices} attempts.")
    if count_of_choices == 7:
      print(f"Dude was that close. Cool got it at the last attempt.")
    break

