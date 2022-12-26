# 6kyu Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# My ideas:
# It is iterable, so I would go through the item/list one by one,
# and take it out of the list if it is already there.

# Idea 1:
def unique_in_order(iterable):
    new_str =[]
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]:
            new_str.append(iterable[i])
    if iterable[-1] != new_str[-1]:
        new_str.append(iterable[-1])
    print(new_str)

# Idea 2:
def unique_in_order(iterable):
    new_str =[]
    if len(iterable)>0:
        new_str.append(iterable[0])
    for i in range(len(iterable)):
        if iterable[i] != new_str[-1]:
            new_str.append(iterable[i])
    print(new_str)

# Best solutions from Codewars:
def unique_in_order(iterable):
    newlist = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

# and
def unique_in_order(iterable):
    result = []
    for item in iterable:
        if len(result) == 0 or item != result[-1]:
            result.append(item)
    return result
        

# unique_in_order('AAAABBBCCDAABBB')
# ['A','B','C','D','A','B'])
