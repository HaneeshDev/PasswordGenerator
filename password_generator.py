import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # print(letters,digits,special_chars)

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars
    
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        
    return pwd

pwd = generate_password(10)

print(pwd)