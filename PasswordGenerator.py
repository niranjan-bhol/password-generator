"""

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    # Define character pools based on user preferences
    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Ensure at least one character pool is selected
    if not char_pool:
        return "Error: No character types selected!"

    # Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

def get_user_preferences():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        return "Error: Length must be an integer!"

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    return length, use_uppercase, use_lowercase, use_numbers, use_symbols

# Main program
if __name__ == "__main__":
    length, use_uppercase, use_lowercase, use_numbers, use_symbols = get_user_preferences()

    if isinstance(length, str):  # Checks if there was an error with the length input
        print(length)
    elif length <= 0 or not (use_uppercase or use_lowercase or use_numbers or use_symbols):
        print("Invalid input: Please ensure that the length is greater than 0 and at least one character type is selected.")
    else:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
        print(f"Generated Password: {password}")

"""

import re
from random import choice

print("\n             --- Password Generator --- \n\n")

string = input("Enter your password for enhancing security : ")

print("\n")

a = r'string'

def search_string_with_regex(file_path, search_string):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        match = re.search(search_string, file_contents)
        return match is not None

file_path = 'password_list.txt'

search_string = a

if search_string_with_regex(file_path, search_string):
    print("Password found in the compromised passwords list, don't worry we will make it strong.")
else:
    print("Well done!! You have a quite strong password, still we will make it unbreakable.")

print("\n")

res = ''.join(choice((str.upper, str.lower))(char) for char in string)

if "a" or "A" in res :
    p1 = res.replace('a','@')
    p1 = p1.replace('A','@')

if "s" or "S" in p1 :
    p1 = p1.replace('s','$')
    p1 = p1.replace('S','$')

if "o" or "O" in p1 :
    p1 = p1.replace('o','0')
    p1 = p1.replace('O','0')

print("Your Entered Password : "+string+"\n")
print("We generated Strong Password : "+p1)