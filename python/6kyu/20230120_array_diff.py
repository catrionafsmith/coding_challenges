#  6kyu Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

# My ideas:
# Need to remove ALL occurrences, whhich would mean that I can't just use remove (as that would only remove the first occurrence)
# Could use list comprehension

def array_diff(a, b):
    return [x for x in a if x not in b]

# Having trouble with the correct syntax for list comprehension, so used stack overflow.
# Was previously trying:
def array_diff(a, b):
    return [a.remove(item) if item in b else item for item in a]


