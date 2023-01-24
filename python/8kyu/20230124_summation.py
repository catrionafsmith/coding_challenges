#  8kyu Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# My ideas:
# use a for loop. For 1 to num sum_tot += i
# use loop comprehension. use sum(loop comprehension)
# Remember that range(num) only includes nim - 1

def summation(num):
    sum_tot = 0
    for i in range(1, num+1):
        sum_tot += i
    return sum_tot

# Refactoring
def summation(num):
    return sum(i for i in range(1, num+1))

# Best practices from Codewars:
# Uses xrange() - only used in python 2.
def summation(num):
    return sum(xrange(num + 1))

# Other best practices - slightly shorter:
def summation(num):
    return sum(range(num + 1))
