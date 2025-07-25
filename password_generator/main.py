import re
import secrets
import string


def generate_password(length = 16, nums = 1, special_chars = 1, uppercase = 1, lowercase = 1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
    
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),            
            (special_chars, fr'[{symbols}]')            
        ]

        # Check constraints
        # count = 0

        # for constraint, pattern in constraints:
        #     if constraint <= len(re.findall(pattern, password)):
        #         count += 1
        #     
        # if count == 4:
        #     break
        # Esta seccion del codigo puede ser reemplazada con la funcion all()

        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

if __name__ == '__main__':
    new_password = generate_password()
    print(f'Generated password: {new_password}')