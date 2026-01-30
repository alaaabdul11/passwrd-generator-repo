import random
import string

def password_generator(length, numbers=True, symbols=True):
    characters = string.ascii_letters

    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def entry():
    try:
        length = int(input("Enter password length (at least 5): "))

        if length < 5:
            print("Password must be at least 5 characters long.")
            return   # stop safely

        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = password_generator(length, numbers, symbols)
        print("\nYour password is:", password)

    except ValueError:
        print("Please enter a valid number.")


entry()

