 import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

l = [rock,paper,scissors]

r = random.randint(0,len(l)-1)

option = int(input("Enter 0 for Rock, 1 for Paper, 2 for scissors!! : "))

user_choice = l[option]
print(f"You chose\n{user_choice}")

sys_choice = l[r]
print(f"Computer chose\n{sys_choice}")

#Impose conditions on the options user choosing for indicating invalid move by some inequality.

if user_choice == sys_choice:
  print("Match Draw")
elif user_choice==l[0] and sys_choice==l[2]:
  print("Rock wins over scissors, User wins!!YAY")
elif user_choice == l[0] and sys_choice == l[1]:
  print("Paper wins against Rock, system wins!")
else:
  print("Scissors wins against paper")
