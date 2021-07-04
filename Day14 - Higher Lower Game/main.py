#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:10:31 2021

@author: datadevil
"""
# Display logo
from data import data
from art import logo, vs
import  random
from replit import clear

print(logo)

#Formatting the account data
#{'name':,'follower count':,'description':,'country':} --> name, descrip, country
def format_data(account):
    '''Takes the account of the celebrity and gives out the formatted neat output'''
    acc_name = account['name']
    acc_fcount = account['follower_count']
    acc_desc = account['description']
    acc_country = account['country']
    
    return (f"{acc_name}, {acc_desc}, from {acc_country}")

def check_ans(guess, a_followers, b_followers):
    '''Takes the both followers count and return if they got it right'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_over = False
accB = random.choice(data)

while game_over == False:
    accA = accB
    accB = random.choice(data)
    
    
    while accA == accB:
        accB = random.choice(data)
    
    
    print(f"Compare A: {format_data(accA)}")
    print(vs)
    print(f"Aganist B: {format_data(accB)}") 
    
    
    #Ask user for the guess
    response = input("Who has more followers? A or B ").lower()
    
    A_fcount = accA['follower_count']
    B_fcount = accB['follower_count']
    
    is_crt = check_ans(response, A_fcount, B_fcount)
    
    clear()
    
    if is_crt:
        print("You're Right")
        score += 1 
        print(f"And your score is {score}")
    else:
        print("Sorry you're wrong")
        print(f"Your final score is {score}")
        game_over = True






    
    
