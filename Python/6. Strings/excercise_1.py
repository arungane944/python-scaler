#palindrom

def is_palindrome(text):
    # Convert the text to lowercase and remove spaces
    text = text.lower().replace(" ", "")
    
    # Check if the text is equal to its reverse
    return text == text[::-1]

# Test the function with a sample string
text = "radar"
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
