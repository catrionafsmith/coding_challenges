#8kyu Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

# First ideas:
# ensure that all items are integers to add them.
# go through the array using a for loop
#  can potentially use loop comprehension.

def sum_mix(arr):
    sum_num = 0
    for item in arr:
        sum_num += int(item)
    return sum_num

# Refactored
def sum_mix(arr):
    return sum(int(x) for x in arr)

# From Codewars:
# using the built in map() function means that you can process and transform all the items in an iterable without using an explicit for loop.
 def sum_mix(arr):
    return sum(map(int, arr))