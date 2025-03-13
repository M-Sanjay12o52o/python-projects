user_input_char = input("Please input your character here: ")

print("User Input Char: ", user_input_char)

# word = ["a", "p", "p", "l", "e"]
word = ["b", "i", "r", "d"]

if user_input_char in word:
  for i in range(len(word)):
    if word[i] == user_input_char:
      print(word[i])
    else:
      print("_")
