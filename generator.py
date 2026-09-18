import random
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    password = "".join(random.choices(chars, k=length))
    return password
print("--- Secure Password Generator ---")
while True:
    user_input = input("Enter desired password length: ")

    try:
        length = int(user_input)
        break
    except ValueError:
        print("Error: That is not a valid number. Please try again. \n")
final_password = generate_password(length)
print("Generated Password: "+ final_password)