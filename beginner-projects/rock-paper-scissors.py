import random 

choices = ["rock", "paper", "scissor"]
attempts = 20

games_count = int(input(f"Enter the number of games that you want to play: "))

result = {"user": 0, "computer": 0}

def determine_winner(player, computer):
  if player == computer:
    return "Draw"
  elif (player == "rock" and computer == "scissor") or (player == "paper" and computer == "rock") or (player == "scissor" and computer == "paper"):
    result["user"] += 1
    return "Player Wins"
  elif (player == "paper" and computer == "scissor") or (player == "rock" and computer == "paper") or (player == "scissor" and computer == "rock"):
    result["computer"] += 1
    return "Computer Wins"
  else:
    return "Invalid choice! Choose rock, paper or scissor."

while games_count > 0:
  computer_choice = random.choice(choices)
  user_choice = input("Enter your choice: (rock, paper, or scissor) ")

  print("User choice: ", user_choice)
  print("Computer choice: ", computer_choice)

  print(determine_winner(user_choice, computer_choice))
  games_count -= 1


print("\nFinal Results: ")
print(f"User Wins: {result['user']}")
print(f"Computer Wins: {result['computer']}")

if result["user"] > result["computer"]:
    print("🎉 You are the overall winner!")
elif result["user"] < result["computer"]:
    print("💻 Computer is the overall winner!")
else:
    print("🤝 It's a Draw!")