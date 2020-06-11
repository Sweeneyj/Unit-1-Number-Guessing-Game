import random
import sys

def get_guess():
  while True:
    try:
      print("Welcome to the number guessing game! ")
      guess = int(input("Please pick a number between 1 and 10: "))
      return guess
    except ValueError:
      print("Not a valid input, please try again.")
      continue
      
def start_game():
  correct_number = random.randint(0, 10)
  guess = get_guess()
  guess_amount = 1
  while True:
    try:
      if guess < correct_number:
        guess_amount += 1         
        guess = int(input("The correct number is larger. Please guess again. "))
      if guess > correct_number:
        guess_amount += 1          
        guess = int(input("The correct number is smaller. Please guess again. "))
      if guess == correct_number:
        print("Nice job you got it! It took you {} attempts to get the correct answer".format(guess_amount))
        break
    except ValueError: 
      print("Not a valid input, please try again.")
      continue
              
  Restart = input("Would you like to play again? Please type Y or N ") 
  while True: 
    try:
      if Restart.lower() == "y": 
        start_game()
      if Restart.lower() == "n": 
        print("Okay well thanks for playing!") 
        sys.exit()  
      if Restart != "y" or Restart != "n":
        Restart = input("Not a valid input please try again. Type Y to play again or N to exit. ")
    except ValueError:
      print("Not a valid input please try again. ")
      continue
start_game()
