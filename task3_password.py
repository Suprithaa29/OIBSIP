import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter the length of the password: "))
use_letters = input("Include letters? (yes/no): ").lower() == "yes"
use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

password = generate_password(length, use_letters, use_numbers, use_symbols)
print("Your generated password is:", password)
