#  6kyu Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# My ideas:
# rule out numm values at start.
# as the arrays can be in any order, I could sort them to get them into order
# I could square each value in array1, and create a new array, sort it and see if it is the same as array2
# could be easy to rule out arrys if the length is different.

def comp(array1, array2):
    if array1 == 0 or array2 == 0:
        return False 
    return sorted([i**2 for i in array1]) == sorted(array2)

# Refactored:
def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False 

# This was the 'best' solution on Codewars

# Alternatives from Codewars:
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

def comp(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x*x for x in a1) == sorted(a2)