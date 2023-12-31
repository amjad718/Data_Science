import re

def is_valid_password(password):
    if len(password) < 6:
        print("Password is too short. It should be at least 6 characters long.")
        return False

    if not re.search(r'[a-z]', password):
        print("Password doesn't contain any lowercase letters (a-z).")
        return False

    if not re.search(r'[A-Z]', password):
        print("Password doesn't contain any uppercase letters (A-Z).")
        return False

    if not re.search(r'[0-9]', password):
        print("Password doesn't contain any digits (0-9).")
        return False

    if not re.search(r'[$#@]', password):
        print("Password doesn't contain any of the special characters ($, #, @).")
        return False

    return True

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please ensure it meets the specified criteria.")