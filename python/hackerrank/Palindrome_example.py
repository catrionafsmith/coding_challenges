Palindrome.py
# Create a function that will tell me if a word is a palindrome.
# Parameters are: take a string. (non-zero) Could there be spaces in it? (e.g. madam i'm adam)
# Return - True if it is a palindrome, False otherwise
# Examples - madam (spaces or punctuation?)
# Ideas: Check if the reverse of a string is the same as the word. Have two pointers that start at either end, and check that they are the same.
# Thoughts about time complexity
# Thoughts about any complexities in this challenge - punctuation and spaces
# Pseudocode:
# Set up a function definition that takes a word as a parameter
def palindrome(word):
# Find the reverse of the word 
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return False
    return True

    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False
# Check if the reverse of the word is the same as the word
# If it is the same, return true, if not then false