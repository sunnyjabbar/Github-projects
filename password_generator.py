import random
import string


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=== Password Generator ===")

while True:
    try:
        length = int(input("Enter password length (8-50): "))

        if 8 <= length <= 50:
            break

        print("Please enter a length between 8 and 50.")

    except ValueError:
        print("Please enter a whole number.")

uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
numbers = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, uppercase, numbers, symbols)

print("\nYour generated password is:")
print(password)
