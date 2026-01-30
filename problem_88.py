# Problem 88: Find all substrings of a string
# Find and fix the error

def all_substrings(text):
    substrings = []
    n = len(text)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(text[i:j])
    return substrings

word = "abc"
print(f"All substrings: {all_substrings(word)}")
