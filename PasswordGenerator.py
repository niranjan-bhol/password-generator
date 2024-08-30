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