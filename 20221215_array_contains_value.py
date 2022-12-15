#  8kyu You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

# My ideas:
# Need to check if something is in something else - is there a function - isIn?
# inIn is not a function - checking syntax, we just use: if XX is in AA:

def check(seq, elem):
    return elem in seq

# No other notable solutions.