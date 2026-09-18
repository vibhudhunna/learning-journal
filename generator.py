import random

def generate_password(length, use_symbols):
    # Check the user's preference for symbols
    if use_symbols == 'yes':
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    else:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
    password = "".join(random.choices(chars, k=length))
    return password

print("--- Secure Password Generator ---")

# 1. Get and validate the length
while True:
    user_input = input("Enter desired password length: ")
    
    try:
        length = int(user_input)
        break
    except ValueError:
        print("Error: That is not a valid number. Please try again.\n")

# 2. Get the symbol preference
symbols_input = input("Include symbols? (yes/no): ").lower()

# 3. Feed both pieces of data into our machine
final_password = generate_password(length, symbols_input)
print("Generated Password: " + final_password)