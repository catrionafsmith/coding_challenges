# Codewars 8kyu
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array 
# (true means present).

# My ideas:
# Use a for loop to count all the sheep, where if the value is True then 1 is added to count.
# Use list comprehension? Doesn't work as it returns a list.
# Use count()
# Use ternary operator?

#  For loop
def count_sheeps(sheep):
    count = 0
    for n in sheep:
        if n == True:
            count += 1
    print(count)
    return count

#  Use count
def count_sheeps(sheep):
    tot_sheep = sheep.count(True)
    print(tot_sheep)
    return tot_sheep

# Factored use of count()
def count_sheeps(sheep):
    return sheep.count(True)

# Use list comprehension? Doesn't work as it returns a list.
# def count_sheeps(sheep):
#     count = 0
#     list_count = [(count += 1) if n == True else count + 0 for n in sheep]
#     print(list_count)
#     return count
#  Output: [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1]

# Use ternary operator - returns 774(?)
# def count_sheeps(sheep):
#     count = 0
#     for n in sheep:
#         count += 1 if n == True else count
#     print(count)
#     return count

herd = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

count_sheeps(herd)

# Other solutions:
# def count_sheeps(sheep):
#   return len([x for x in sheep if x])

# def count_sheeps(herd):
#   return sum(1 for sheep in herd if sheep)