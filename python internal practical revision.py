text=input("Enter text: ")
key=int(input("Enter the key: "))
encrypted=""
for char in text:
    if char.isupper():
        encrypted=encrypted+chr((ord('A')+ord(char)+key)%26+ord('A'))
        