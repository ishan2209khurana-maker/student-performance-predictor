text = input("Enter message: ")
key = int(input("Enter the key: "))
encrypted = ""

for ch in text:
    if ch.isupper():
        encrypted = encrypted + chr((ord(ch) - ord('A') + key) % 26 + ord('A')) # encrypted=""+ chr(76)
    elif ch.islower():
        encrypted = encrypted + chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
        encrypted = encrypted + ch
print("Encrypted message: ", encrypted)

# decryption
decrypted = ""
for ch in encrypted:
    if ch.isupper():
        decrypted = decrypted + chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
    elif ch.islower():
        decrypted = decrypted + chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
    else:
        decrypted = decrypted + ch
print("Decrypted message: ", decrypted)