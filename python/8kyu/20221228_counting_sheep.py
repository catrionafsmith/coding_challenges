# 8kyu Given a non-negative integer, 3 for example, return a string with a murmur: 
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
# My ideas - iterate through a for loop
# *Remember to use f string

# Initial solution:
def count_sheep(n):
    sheep_string=""
    for i in range(1, n+1):
        sheep_string += f"{i} sheep..."
    return sheep_string

# Refactored:
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

# Codewars solutions:
# Using lambda:
count_sheep = lambda __:''.join('%i sheep...'%(_+1) for _ in range(__))

# Using format
def count_sheep(n):
    if n == 1:
        return "1 sheep..."
    else:
        return count_sheep(n - 1) + "{} sheep...".format(n)