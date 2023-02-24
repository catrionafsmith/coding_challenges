#
# 1. Palindrome Index
# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

# Ideas:
# Go through the string, removing each letter in turn and Test to see if the string and the reverse string are the same
# s without letter = s.pop(letter)
# or s.remove(i)
# print(s.replace('a', ''))

def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)):
        new_s = s[:i] +  s[i+1:]
        if new_s == new_s[::-1]:
            return i
    return -1

print(palindromeIndex("aaab"))