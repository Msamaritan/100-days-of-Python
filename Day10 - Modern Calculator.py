#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:28:07 2021

@author: datadevil
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

def calculator():
  num1 = float(input("Enter the first number : "))
  operations = {"+":add, "-":sub,"*":mul,"/":div}
  for keys in operations:
    print(keys, end="\t")
  print("\n")
  should_continue = True
  while should_continue:
    oper_sym = input("Which operations do you want to perform? ")
    if oper_sym in operations:
      num2 = float(input("Enter the next number : "))

      cal_fun = operations[oper_sym]
      ans = cal_fun(num1,num2)
      print(f"{num1} {oper_sym} {num2} is {ans}")

      if input("Enter 'y' to continue with the {ans} or 'n' to start a new calculation : ") == 'y':
        num1 = ans
      else:
        should_continue = False
        calculator()
    else:
      print("Enter a valid operation")
      

calculator()