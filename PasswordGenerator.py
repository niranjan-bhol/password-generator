import random
import string

# Get the length of the password from the user
length = int(input("Enter the length of the password: "))

# Define the character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for i in range(length))

# Printing the password
print("Generated password:", password)