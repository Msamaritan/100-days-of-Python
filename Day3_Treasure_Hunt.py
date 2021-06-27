print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("The Objective of the game is to atleast one of your crew member should open the treasure!")
num_persons = int(input("How many members you want to help yourself in this treasure hunt?\n"))
dir = input("You are in a Jungle, lost, do you all want to take left or right??\n")
if dir.lower() == "right":
  s_or_w = input("You have reached the lake, do you want to swim or wait for the boat?\n")
  if s_or_w.lower() == "wait":
    door = input("You have reached the magical three doors!! Which one do you want to open? Blue door? Yellow door? Red Door?\n")
    if door.lower() == "blue":
      print("Game Over! You have entered the room of Beasts and they ate you!!")
    elif door.lower() == "yellow":
      print("Game over! You have entered the room of fire.")
    else:
      print("You won! You have entered the room of treasure.")
  else:
    print("Game Over! You became a dinner for the shark")
else:
  print("The first guy fell inside a hunter trap! Oopsie!! Thank god y'all noticed and moved back")
  print("The remaining crew took a route and reached to the lake")
  num_persons -= 1
  s_or_w = input("You have reached the lake, do you want to swim or wait for the boat?\n")
  if s_or_w.lower() == "wait":
    door = input("You have reached the magical three doors!! Which one do you want to open? Blue door? Yellow door? Red Door?\n")
    if door.lower() == "blue":
      print("Game Over! You have entered the room of Beasts and they ate you!!")
    elif door.lower() == "yellow":
      print("Game over! You have entered the room of fire.")
    else:
      print("You won! You have entered the room of treasure.")
  else:
    print("Game Over! you all became a tasty dinner for Mr.Shark!")
  






#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
