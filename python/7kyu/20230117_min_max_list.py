#  7kyu Write a function that returns both the minimum and maximum number of the given list/array.

# My ideas - format answer of min(lst) and max(lst).
# *format() is only for string outputs
# Do I need to make a copy of the list?

# First try
def min_max(lst):
    new_list = []
    new_list.append(min(lst))
    new_list.append(max(lst))
    return new_list

# Refactored
def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1,2,3,4,5]))

# This solution was the same as the Codewars best practice.