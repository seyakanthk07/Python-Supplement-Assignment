# Problem 89: Check if number is palindrome
# Find and fix the error

def is_palindrome_number(n):
    original = str(n)
    reversed_num = original[::-1]
    return original == reversed_num

print(f"Is 121 palindrome? {is_palindrome_number(121)}")
