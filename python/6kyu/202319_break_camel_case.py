#  6kyu Complete the solution so that the function will break up 
# camel casing, using a space between words.

# My ideas:
# Use ascii Upper case string method and a loop to see if there are any 
# upper case characters, and if so, split and return the first section.
# or add space before upper case character
# First try - not working - not sure if split is working, and it is returning too early.
import string
# def solution(s):
#     for char in s:
#         if char in string.ascii_uppercase:
#             s = s.split(char)
#             return " ".join(s)
#         else:
#             return s



def solution(s):
    new_str = ""
    for char in s:
        if char in string.ascii_uppercase:
            new_str += " " + char
        else:
            new_str += char
    return new_str


# Codewars best solution:
# List comprehension syntax. 
# Do this if this else that for item in list

def solution(s):
    return "".join(" " + char if char in string.ascii_uppercase else char for char in s)
    

print(solution("helloWorld"))
