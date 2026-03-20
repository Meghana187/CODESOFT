#-*-coding:utf-8-*-
import random
import string

print("🔐 PASSWORD GENERATOR")

length = int(input("Enter password length: "))
if length <= 0:
    print("Please enter a valid length!")
    exit()

print("\nInclude in password:")
use_upper = input("Uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Special characters? (y/n): ").lower() == 'y'

characters = ""

if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("Error: No character types selected!")
    exit()

def generate_password(characters, length):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
password = generate_password(characters, length)
print("\nGenerated Password:", password)