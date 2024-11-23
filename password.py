import string
import random


alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
all_characters = alphabets + digits + special_characters

def generate_random_password():
   
    length = int(input("Enter password length: "))
    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))
    
    
    total_characters = alphabets_count + digits_count + special_characters_count
    if total_characters > length:
        print("Error: Total characters exceed the password length.")
        return
    
    
    password = []
    password.extend(random.choices(alphabets, k=alphabets_count))
    password.extend(random.choices(digits, k=digits_count))
    password.extend(random.choices(special_characters, k=special_characters_count))
    
    # Add random characters to fill the password length
    if total_characters < length:
        password.extend(random.choices(all_characters, k=length - total_characters))
    
    # Shuffle the password for randomness
    random.shuffle(password)
    
    # Convert the list to a string and display the password
    print("Generated Password:", "".join(password))


generate_random_password()
