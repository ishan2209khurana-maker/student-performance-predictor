# Open the file
f = open("new.txt", "r")

text = f.read()
f.close()

# Stopwords
stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "on"}

# Convert text into words
words = text.lower().split()

# Dictionary to store frequency
frequency = {}

for word in words:
    if word not in stopwords:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

# Ask for N 
n = int(input("Enter N: "))
# Sort words according to frequency
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Print Top N words
print("Top", n, "frequent words:")

for word, count in sorted_words[:n]:
    print(word, ":", count)