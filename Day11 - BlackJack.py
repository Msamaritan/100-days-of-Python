#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:47:26 2021

@author: datadevil
"""
import random


def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card

def cal_score(cards):
    '''Return the sum of cards, also check the blackjack condition'''
    if (11 in cards) and (10 in cards) and (len(cards)==2):
        return 0
    
    if (11 in cards) and (sum(cards) >21):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)
 
def compare(user_sum, pc_sum):
    '''Compares all Different conditions and decides the winner''' 
    if user_sum == pc_sum:
        return "Game Draw! Oopsie!!"
    elif pc_sum == 0:
        return "You lose, Oppenent had a BlackJack"
    elif user_sum == 0:
        return "You win!! BlackJack!!!"
    elif user_sum > 21:
        return "Score reached above 21, You lose"
    elif pc_sum > 21:
        return "PC score is above 21, PC lose"
    elif user_sum > pc_sum:
        return "You win"
    else:
        return "PC wins"

def blackJack():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __.
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
        ."""
    print(logo)
    user_cards = []
    pc_cards = []
    is_GameOver = False
    
    for i in range(0,2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())
    
    print(f"Your Hand: {user_cards}")
    print(f"PC Hand: {pc_cards}")
    
    while not is_GameOver:
        user_sum = cal_score(user_cards)
        pc_sum = cal_score(pc_cards)
        
        print(f"Your Score {user_sum}, PC score {pc_sum}")
        print(f"PC First card {pc_cards[0]}")
        
        if user_sum == 0 or pc_sum==0 or user_sum>21:
            is_GameOver = True
            
        else :
            user_res = input("Draw another card? Type 'yes' or 'no':").lower()
            if user_res == "yes":
                user_cards.append(deal_card())
            else:
                is_GameOver = True
    
    while pc_sum!=0 and pc_sum<17:
        pc_cards.append(deal_card())
        pc_sum = cal_score(pc_cards)
            
    print(f"You final Hand : {user_cards}")
    print(f"PC Final Hand is : {pc_cards}")
    print(compare(user_sum, pc_sum))
             

while input("Do you want to play the BLACKJACK game, type 'yes' or 'no': ").lower() == "yes":
    blackJack()
    
print("Thanks for playing the game!")


