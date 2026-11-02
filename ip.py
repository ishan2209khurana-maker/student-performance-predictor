text=input("Enter string: ")
c=text.replace(" ","").lower()
if c[::-1]==c:
    print("String is a palindrome")
else:
    print("String is not palindrome")
freq={}
for char in c:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("\n character frequencies: ")
for char,count in freq.items():
    print(char,":",count)
