# 7kyu Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# My ideas:
# find minimum of array
# find the index of that minimum
# remove the item at that index
#  - use the value to pop it (will this pop all of them?)
#  - use the index to remove it

def remove_smallest(numbers):
    smol = min(numbers)
    numbers.remove((smol))
    return numbers

if __name__ == "__main__":
    print(remove_smallest([11, 27, 3, 4, 5]))

# N.B. Assertion is that list should not be mutated:
#  Can make a shallow copy of the list to get over this
def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        copy_num = numbers[:]
        copy_num.remove((min(copy_num)))
    return copy_num

# Best solutions from Codewars:
def remove_smallest(numbers):
    # making the copy
    a = numbers[:]
    # if a exists (is not an empty list)
    if a:
        # remove the min item from list a
        a.remove(min(a))
    return a



