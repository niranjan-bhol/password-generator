import random
import string

def generate_password(length):
    # Define the character set: lowercase, uppercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Get the desired length of the password from the user
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        password = generate_password(length)
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid integer for the password length.")