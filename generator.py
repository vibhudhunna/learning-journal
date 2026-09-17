import random
print("--- Secure Password Generator ---")
user_input = input("Enter desired password length: ")
try:
    length = int(user_input)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    password = "".join(random.sample(chars, length))
    print("Generated Password: " + password)
except ValueError:
    print("Error: That is not a valid number. Please use digits")