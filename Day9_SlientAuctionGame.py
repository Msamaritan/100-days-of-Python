#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:59:49 2021

Description : The slient auction game simulator, where bidders bid their amount
              and the highest bidder is the winner!

@author: datadevil
"""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def highest_bidder(bidd):
    maxi = 0
    for keys in bidd:
        bidding_amt = bidd[keys]
        if bidding_amt > maxi:
            maxi = bidding_amt
            winner = keys 
    print(f"The highest bidder is {winner} and the bid is INR {maxi}")
        
flag = True
bidder = {}
while flag == True:
    name = input("Enter Your name: ")
    bid_amt = int(input("Enter the amount: INR "))
    response = input("Is there anybody left? Type Yes or No \n").lower()
    bidder[name] = bid_amt
    
    
    if response=="no":
        flag = False

print(bidder)
highest_bidder(bidder)

  