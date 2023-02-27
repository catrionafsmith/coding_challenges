# We say a sequence of brackets is balanced if the following conditions are met:
#
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.


# Ideas:
# string must be a palindrome.
# len(str) cannot be odd

def isBalanced(s):
    if len(s)%2 != 0:
        return "NO"
    if s == s[::-1]:
        return"YES"

print(isBalanced("{[()]}"))