#  8 kyu Complete the solution so that it reverses the string passed into it.

# My ideas:
# Is there a string function that reverses?
# Could change it to a list, then reverse the list and join.
# Could loop through the word from the last character and create a new string.

def solution(string):
    return string[::-1]

print(solution('world'))