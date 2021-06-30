#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for i in range(1,nr_letters+1):
   password += random.choice(letters)


for j in range(1, nr_symbols+1):
  r2 = random.choice(symbols)
  password = password + r2
  
# for k in range(0,nr_numbers):
#   r3 = random.choice(numbers)
#   password = password + r3

for k in range(1,nr_numbers+1):
  r3 = random.randint(0,len(numbers))
  password = password + numbers[r3]

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for i in range(1,nr_letters+1):
  password_list += random.choice(letters)

for j in range(1, nr_symbols+1):
  password_list += random.choice(symbols)
  
for k in range(1,nr_numbers+1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

#Converting the list into strings
password = ""
for i in password_list:
  password += i

print(password)
