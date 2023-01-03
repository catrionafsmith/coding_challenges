# 6kyu Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]

# My ideas:
# bottom floor is the longest, is = n
# Each floor is a string, separated by a comma in a list
# Pattern is 1, 3, 5, 7. Odd numbers. floor numb * 2-1

def tower_builder(n):
    tower = []
    floor_string = ""
    for i in range(1, n+1):
        floor_string = " "*(n-i) + "*"*(2*i-1) + " "*(n-i)
        tower.append(floor_string)
    return tower

print(tower_builder(6))  
# First try - needed to change the number of * to 2i-1 from just i ;)  
[
    '     *     ', 
    '    **    ', 
    '   ***   ', 
    '  ****  ', 
    ' ***** ', 
    '******']
[
    '     *     ', 
    '    ***    ', 
    '   *****   ', 
    '  *******  ', 
    ' ********* ', 
    '***********'
    ]

# Refactored
def tower_builder2(n):
    return [(" "*(n-i) + "*"*(2*i-1) + " "*(n-i)) for i in range(1, n+1)]

print(tower_builder2(6))

# Best solution from Codewars:
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# New information - can use .center() to centre something in a line.