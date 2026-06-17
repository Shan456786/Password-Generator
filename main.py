import random
import string

def generate_password(length=12):
    
    all_characters = (
        string.ascii_lowercase + 
        string.ascii_uppercase + 
        string.digits + 
        string.punctuation
    )
    

    password_list = [random.choice(all_characters) for _ in range(length)]
    
    password = "".join(password_list)
    
    return password


password_length = int(input("Enter the desired password length: "))


new_password = generate_password(password_length)
print(f"Your secure password is: {new_password}")
