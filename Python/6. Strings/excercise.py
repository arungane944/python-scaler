#print all the vowels in string

text = "I apologize if there was any confusion. How can I assist you with a specific question or topic?"

vowels = "aeiou"

# Convert text to lowercase for case-insensitive comparison
text = text.lower()

for char in text:
    if char in vowels:
        print(char)