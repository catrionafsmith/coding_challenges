#  8kyu Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# My ideas:
# use a for loop to multiply each number and then add to a list.
# refactor to show list comprehension.

# Initial solution
def count_by(x, n):
    mult_list = []
    for i in range(1, n+1):
        mult_list.append(x*i)
    return mult_list

# Refactored
def count_by(x, n): 
    return [(x*i) for i in range(1, n+1)]

# Best solution from CodeWars - using the range function with a step of x:
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return range(x, x * n + 1, x)