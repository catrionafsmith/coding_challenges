# 7kyu Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# My ideas:
# I can sum an array
# I can use the modulo to determine if a number is odd or even
# Need to return as a string
# Try ternary statement?

# First try:
def odd_or_even(arr):
    sum_arr = sum(arr)
    if sum_arr % 2 == 0:
        return "even"
    else:
        return "odd"

# Refactored:
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

# From Codewars:
# Using a lambda function:
oddOrEven = lambda a: ['even','odd'][sum(a)%2]
# another alternative:
def odd_or_even(arr):
    return ['even','odd'][sum(arr)%2]


