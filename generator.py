import random
print("--- Secure Password Generator ---")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
password = "".join(random.sample(chars, 16))
print("Generated Password: " + password)
