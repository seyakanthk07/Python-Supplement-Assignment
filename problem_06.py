# Problem 6: Reverse a string
# Find and fix the error

text = "Python"
reversed_text = ""
for i in range(len(text), 0, -1):
    reversed_text += text[i-1]
print(f"Reversed: {reversed_text}")
