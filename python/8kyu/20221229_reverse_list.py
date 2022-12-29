# 8kyu Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]

# My ideas:
# append items to a list using the range function and in reverse order(reverse step).

# First try:
def reverse_seq(n):
    num_list = []
    for i in range(n, 0, -1):
        num_list.append(i)
    return num_list

# Refactored:
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]

# Best on Codewars:
# You can use list() function to create a list
def reverse_seq(n):
    return list(range(n, 0, -1))

# or just return the range!
def reverseseq(n):
    return range(n, 0, -1)