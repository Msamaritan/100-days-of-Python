#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:57:37 2021

Description : Caeser Cipher, we can shift the letters by a specified unit in the alphabetical
              order and we can also decode the encoded code in the same program 
              but the decoding person must know the encode shift(secret key)

@author: datadevil
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        # We are checking that the user enters only the alphabets
        position = alphabet.index(char)
        new_position = (position + shift_amount)%26
        end_text += alphabet[new_position]
    else:
      end_text+=char
      
  print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)


while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  response = input("Do you want to restart the cipher program?").lower()
  
  if response == "no":
    break