#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:40:45 2021

@author: datadevil
"""
import random
import hangman_words
from hangman_art import logo,stages

#from replit import clear

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = len(stages)-1 

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #To clear the screen after each input
    #clear()
    
    if guess in display:
        print("You have already entered the letter, Try with another one!")
        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 
    print(f"{' '.join(display)}")
    #Join all the elements in the list and turn it into a String.
    
    
    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print("The guessed letter is not in the word, guess another one wisely, you are running out of lives")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])

    
     