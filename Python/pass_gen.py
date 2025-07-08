import string
import random

def generate_password(length=12, use_digits=True, use_symbols=True, use_upper=True, use_lower=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    charset = ""
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase

    if not charset:
        raise ValueError("No character sets selected!")

    # Ensure at least one character from each selected type
    password = []
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))

    # Fill the rest of the password length
    password += random.choices(charset, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

# Example usage:
print(generate_password(length=16, use_digits=True, use_symbols=True))
