"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys
Guess = 0
print("""
  Friends, Romans, and countrymen! Welcome to Frankies Number Guessing Game! Please guess a number between 1 and 10 
  """)
def validate_guess():
  global Guess 
  Guess = input("Pick a number between 1 and 10: ")
  while True: 
    try:
      val = int(Guess) 
      break; 
    except ValueError: 
      print("This is not a number. Please enter a valid Number") 
      Guess = input("Pick a number between 1 and 10: ") 
def start_game():
  CorrectNumber = random.randint(1, 10)
  global Guess
  GuessAmount = 1
  Guess = int(Guess)
  while True:
    if Guess > CorrectNumber: 
      Guess = input("Number is too big, guess again: ")
      Guess = int(Guess)
      GuessAmount = GuessAmount + 1
      continue
    elif Guess < CorrectNumber: 
      Guess = input("Number is too low, guess again: ")
      Guess = int(Guess)
      GuessAmount = GuessAmount + 1
      continue
    elif Guess == CorrectNumber: 
      print("Got it! Nice Job It took {} tries".format(GuessAmount))
      break
  Restart = input("Would you like to play again? Type Y or N. ") 
  while True: 
    if Restart.lower() == "y": 
      validate_guess()
      start_game()
    elif Restart.lower() == "n": 
      print("Okay well thanks for playing!") 
      sys.exit() 
validate_guess()
start_game()

  
  
  
  
  
  