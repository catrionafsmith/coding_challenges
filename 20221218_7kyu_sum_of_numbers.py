# 7kyu Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!

# ideas - make the numbers into a list, then sum the list.
# use the range function

# My solution:
def get_sum(a,b):
    if a > b:
        return sum(range(b, a+1))
    else: 
        return sum(range(a, b+1))

# refactored:
def get_sum(a,b):
    return sum(range(b, a+1)) if a > b else sum(range(a, b+1))

# Codewars best practice:
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))