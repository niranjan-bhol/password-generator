import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from below : 
      1. Letters
      2. Digits
      3. Special Characters
      4. Exit''')

characterList = ""

# Getiing character set for password
while(True):
    
    choice = int(input("Enter your choice: "))
    
    if(choice == 1):
        # Adding letters to possible characters
        characterList += string.ascii_letters
        
    elif(choice == 2):
        # Adding digits to possible characters
        characterList += string.digits
        
    elif(choice == 3):
        # Adding special characters to possible characters
        characterList += string.punctuation
        
    elif(choice == 4):
        break
    
    else:
        print("Please enter a valid option")

password = []

for i in range(length):

    # Picking a random character from characterList
    random_char = random.choice(characterList)

    # Appending a random character to password
    password.append(random_char)

# printing password as a string
print("The generated random password is " + ''.join(password))