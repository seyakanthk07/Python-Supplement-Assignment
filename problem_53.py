# Problem 53: Check if two strings are anagrams
# Find and fix the error

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1.lower()) == sorted(str2.lower())

word1 = "Listen"
word2 = "Silent"
print(f"Are anagrams: {are_anagrams(word1, word2)}")
