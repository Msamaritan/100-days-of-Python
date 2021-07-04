#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:13:44 2021

@author: datadevil
"""

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random

def Game_logic(attempts_left,crt_number):
  for i in range(0,attempts_left):
    guess_number = int(input("Make a guess: "))
      
    if guess_number<crt_number:
      attempts_left -= 1
      print(f"Too Low")
      if attempts_left!=0:
        print("Guess Again")
        print(f"You have only {attempts_left} attempts left!")

    elif guess_number > crt_number and attempts_left!=0:
      attempts_left -= 1
      print("Too High")
      if attempts_left!=0:
        print("Guess Again")
        print(f"You have only {attempts_left} attempts left!")
        
    else:
      print(f"You got it, the answer is indeed {guess_number}")
      break
      
    if attempts_left == 0 :
      print("You've run out of attempts!")
      break

logo ='''

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || | _____  _____ | || |  _________   | || |    _______   | || |    _______   | |
| |  .' ___  |   | || ||_   _||_   _|| || | |_   ___  |  | || |   /  ___  |  | || |   /  ___  |  | |
| | / .'   \_|   | || |  | |    | |  | || |   | |_  \_|  | || |  |  (__ \_|  | || |  |  (__ \_|  | |
| | | |    ____  | || |  | '    ' |  | || |   |  _|  _   | || |   '.___`-.   | || |   '.___`-.   | |
| | \ `.___]  _| | || |   \ `--' /   | || |  _| |___/ |  | || |  |`\____) |  | || |  |`\____) |  | |
| |  `._____.'   | || |    `.__.'    | || | |_________|  | || |  |_______.'  | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''
print(logo)
print("Welcome to the number guessing game!!")
print("Im think of number between 1 and 100, can you guess it?")
 
l = list(range(0,101))
crt_number = random.choice(l)
level = input("Choose the difficulty level, 'Hard' or 'easy': ").lower()
#print(f"Correct number {crt_number}")

if level == "easy":
  Game_logic(10,crt_number)
elif level == "hard":
  Game_logic(5,crt_number)



        



