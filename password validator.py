# It has at least 8 characters
# It contains at least one uppercase letter
# It contains at least one lowercase letter
# It contains at least one digit
# It contains at least one special character (non-alphanumeric)

import re

def password_check(password):
#   Define a function that takes in a password and checks if it meets certain criteria (e.g., length, use of special characters, etc.).
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True



def main ():
#   Define a main function that prompts the user for input, obtains the user's input, and calls the function from step 1 with the user's input.
#   Call the main function to start the password validator.
    password = input("Enter a password: ")
    
    while password_check(password) != True:
        print("Invalid, try a different password")
        password = input("Enter a password: ")
    else: 
        print("Valid password")
main ()