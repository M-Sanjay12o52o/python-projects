import random
import time

game_num = 21

number_of_players = int(input("Enter the number of players playing the game (1, 2, or 3): "))

user_input = 0

if number_of_players == 1:
    who_goes_first = int(input("Enter who goes first. 1 for You, 2 for Computer: "))
    if who_goes_first == 1:
        while game_num > 0:
          time.sleep(1)
          user_input = int(input("Enter your num: "))
          if (user_input == 21):
            print("You lost.")
            break
          print("Your Input: ", user_input)
          game_num -= 1
          time.sleep(1) # waiting for 1 second before computer input prints
          if (user_input + 1 == 21):
            print("You Won.")
            break
          print("Computer Input: ", user_input + 1)
          game_num -= 1
    elif who_goes_first == 2:
        computer_input = 1
        while game_num > 0:
                    
          if computer_input == 1:
            print("Computer input: ", computer_input)
            game_num -= 1
          else:
            computer_input += 1
            if computer_input == 21:
              print("Computer Input: ", computer_input)
              print("You Won.")
              break
            print("Computer Input: ", computer_input)
            game_num -= 1
          time.sleep(1)
          user_input = int(input("Enter your num: "))
          print("Your Input: ", user_input)
          time.sleep(1)
          computer_input += 1
          game_num -= 1

elif number_of_players == 2:
    user_name1 = input("Please enter player one name: ")
    user_name2 = input("Please enter player two name: ")
    
    first = input(f"Who goes first, {user_name1} or {user_name2}?: ")
    second = user_name1 if first == user_name2 else user_name2
    
    while game_num > 0:
        for player in [first, second]:
            user_input = int(input(f"{player}, enter a number: "))
            game_num -= 1
            print(f"Remaining: {game_num}")
            if game_num <= 0:
                print(f"{player} loses!")
                exit()

elif number_of_players == 3:
    user_name1 = input("Please enter player one name: ")
    user_name2 = input("Please enter player two name: ")
    user_name3 = input("Please enter player three name: ")
    
    first = input(f"Who goes first, {user_name1}, {user_name2}, or {user_name3}?: ")
    second = input(f"Who goes second, {user_name1}, {user_name2}, or {user_name3}?: ")
    players = [user_name1, user_name2, user_name3]

    players.remove(first)
    players.remove(second)

    goes_first = first
    goes_second = second
    goes_third = players[0]
    
    while game_num > 0:
        for player in [goes_first, goes_second, goes_third]:
            user_input = int(input(f"{player}, enter a number: "))
            game_num -= 1
            print(f"Remaining: {game_num}")
            if game_num <= 0:
                print(f"{player} loses!")
                exit()