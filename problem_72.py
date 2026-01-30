# Problem 72: Count uppercase and lowercase letters
# Find and fix the error

def count_case(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if 'A' <= char <= 'Z':
            upper_count += 1
        elif 'a' <= char <= 'z':
            lower_count += 1
    return upper_count, lower_count
sentence = "Hello World"
u, l = count_case(sentence)
print(f"Uppercase: {u}, Lowercase: {l}")
