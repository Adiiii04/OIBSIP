import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one type of characters!")
        return None

    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

def get_yes_no(prompt):
    return input(prompt).strip().lower() == 'y'

def main():
    print("=== Password Generator ===")

    while True:
        length_input = input("Enter password length: ")
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        else:
            print("Please enter a positive number.")

    letters = get_yes_no("Include letters? (y/n): ")
    numbers = get_yes_no("Include numbers? (y/n): ")
    symbols = get_yes_no("Include symbols? (y/n): ")

    password = generate_password(length, letters, numbers, symbols)
    if password:
        print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    main()
