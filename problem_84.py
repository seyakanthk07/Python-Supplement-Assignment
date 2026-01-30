# Problem 84: Check if substring exists
# Find and fix the error

def contains_substring(text, substr):
    return substr in text

sentence = "Python programming is fun"
print(f"Contains 'fun': {contains_substring(sentence, 'fun')}")
