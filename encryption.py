import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"keys: {key}")

#Encryption:
og = input("Enter a line to encrypt: ")
new = ""
for letter in og:
    index = chars.index(letter)
    new += key[index]

print(og)
print(new)

#Decryption:
new1 = input("Enter a line to decrypt: ")
og1 = ""

for letter in new1:
    index = keys.index[letter]
    og1 += chars[index]

print(new1)
print(og1)