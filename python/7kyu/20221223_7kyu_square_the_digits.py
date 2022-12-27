#7kyu square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# My ideas:
# Could use string concatenation, treat each digit as a string, square it, and then concatenate back together.
# Could split it into a list, then square it, then join the list?
# could split it using place value, using the modulo, then rejoin.

def square_digits(num):
    string = str(num)
    con_string = ""
    for letter in string:
        square = (int(letter))**2
        con_string += str(square)
    return int(con_string)

def square_digits(num):
    sq_string = ""
    for i in iter(str(num)):
        sq_string += str(int(i)**2)
    return int(sq_string)

# trying out solution including list iteration
num = 9119
thing = ((int(i)**2) for i in (iter(str(num))))
print(thing)

# Best solution from Codewars:
# My solution (2) above, plus the solution below with list iteration.
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# Learning points from today:
# I can typecast an integer to a string to iterate through each digit.
# I can use for i in iter(str(num)) or use for d in str(num)
# Also learned the vocabulary 'typecast' for Python!