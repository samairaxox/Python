import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','@','#','$','%','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome to password generator!")
my_letters = int(input("How many letters?"))
my_symbols = int(input("How many symbols?"))
my_numbers = int(input("How many numbers"))
password_list = []
for char in range(0,my_letters):
    password_list.append(random.choice(letters))
for char in range(0,my_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,my_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(password)
