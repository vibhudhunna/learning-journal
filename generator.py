import random
print("--- Secure Password Generator ---")
while True:
    user_input = input("Enter desired password length: ")
    try:
        length = int(user_input)
        break
    except ValueError:
        print("Error: That is not a valid number. Please use digits")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
password = "".join(random.sample(chars, length))
print("Generated Password: " + password)