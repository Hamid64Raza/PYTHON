import re

def is_strong_password(password):

    if len(password) < 8:
        return False
    
    
    if not re.search('[a-z]', password) or not re.search(r'[A-Z]', password):
        return False
    

    if not re.search(r'\d', password):
        return False
    

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True


password = input("Enter a password: ")

if is_strong_password(password):
    print("Strong password!")
else:
    print("Weak password. Make it stronger.")
