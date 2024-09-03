import string
import random

global password

def start():
    print("\n\n             --- Password Generator --- \n\n")

def choice_input():
    print("Enter 1 to generate a random password\nEnter 2 to check the password\nEnter 3 to generate a meaningful, memorable password\n")

def input_choice():
    ch = input("Input : ")
    return ch

def get_user_preferences():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        return "Error: Length must be an integer!"
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
    
    print(" ")
    
    return length, use_uppercase, use_lowercase, use_numbers, use_symbols

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

def check_password_in_pwned_list(password: str, filename: str = '10-million-password-list-top-1000000.txt') -> bool:
    """
    Checks if the provided password is present in the pwned passwords list.
    
    Args:
        password (str): The password to check.
        filename (str): The name of the file containing the pwned passwords list.
        
        Returns:
        bool: True if the password is pwned, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            passwordlist = file.read().splitlines()
            
            return password in passwordlist
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return False

def modify_password(password):
    password1 = password.replace('a', '@').replace('A', '@')
    password1 = password1.replace('i', '!').replace('I', '!')
    password1 = password1.replace('l', '|').replace('L', '|')
    password1 = password1.replace('s', '$').replace('S', '$')
    password1 = password1.replace('o', '0').replace('O', '0')
    
    print("Your password : "+password)
    print("We generated strong password : "+password1)

def generate_password_custom():
    password = input("Enter your existing password or word to convert it into strong password : ")
    print("")
    password1 = password.replace('a', '@').replace('A', '@')
    password1 = password1.replace('i', '!').replace('I', '!')
    password1 = password1.replace('l', '|').replace('L', '|')
    password1 = password1.replace('s', '$').replace('S', '$')
    password1 = password1.replace('o', '0').replace('O', '0')
    
    print("Generated meaningful, memorable strong password : "+password1)

def switch_case(value):
    if value == "1":
        
        length, use_uppercase, use_lowercase, use_numbers, use_symbols = get_user_preferences()
        
        if isinstance(length, str):  # Checks if there was an error with the length input
            print(length)
        elif length <= 0 or not (use_uppercase or use_lowercase or use_numbers or use_symbols):
            print("Invalid input: Please ensure that the length is greater than 0 and at least one character type is selected.")
        else:
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
            print(f"Generated Password : {password}")
    
    elif value == "2":
        
        password = input("Enter the password to check: ")
        print("")
        
        if check_password_in_pwned_list(password):
            print("This password found in the compromised password list, please choose a different one or give us a chance, we will make it strong.\n")
        else:
            print("This password is not in the compromised password list and is safe to use, still, you can give us a chance, we will make it unbreakable.\n")
        
        ch1 = input("Enter 'y' to make it strong, any other key to exit : ")
        print("")
        
        if ch1 == 'y':
            modify_password(password)
        else:
            pass
    
    elif value == "3":
        generate_password_custom()
    else:
        print("\nInvalid choice. Please enter valid choice.\n")
        # Re-prompt the user for input one more time
        new_choice = input_choice()
        if new_choice in ["1", "2", "3"]:
            switch_case(new_choice)
        else:
            print("\nInvalid choice entered again. Exiting.\n")

# Main program
if __name__ == "__main__":
    start()
    choice_input()
    choice_ = input_choice()
    switch_case(choice_)
