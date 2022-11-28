# Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the number passed to your function. Or, in other words, sum all the even Fibonacci numbers that are lower than the given number n (n is not the nth element of Fibonnacci sequence) without including n.
# The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:
# 0 1 1 2 3 5 8 13 21...
# For example:
# eve_fib(0)==0
# eve_fib(33)==10
# eve_fib(25997544)==19544084

# My ideas:
# Make an array of ficonacci numbers up to n, then test all of the numbers for % 2, then sum.
# Remember that m is not the nth number in the fibonacci series.

# To generate the fibonacci series:
# def even_fib(m):
#     fib =[0, 1]
#     a = 0
#     b = 1
#     for i in range(m):
#         fib.append(a + b)
#         c = a+b
#         a = b
#         b = c
#     print(fib)

# even_fib(4)

# Creates fibonacci sequence and sums even numbers. Generates more numbers in the sequence than are required. 
# def even_fib(m):
#     fib =[0, 1]
#     a = 0
#     b = 1
#     for i in range(m):
#         fib.append(a + b)
#         c = a+b
#         a = b
#         b = c
#     print(fib)
#     sum = 0
#     for n in fib:
#         if n % 2 == 0:
#             sum += n
#     print(sum)


# even_fib(4)

def even_fib(m):
    a = 0
    b = 1
    fib =[a, b]
    while (a+b) < m:
        fib.append(a + b)
        c = a+b
        a = b
        b = c
    sum = 0
    for n in fib:
        if n % 2 == 0:
            sum += n
    print(sum)


even_fib(25997544)

# Best Practices examples for Codewars:
# def even_fib(m):
#     x,y = 0, 1
#     counter = 0
#     while y < m:
#         if y % 2 == 0:
#             counter += y
#         x,y = y, x+ y
#     return counter

# Similar example:
# def even_fib(m):
#     """Returns the sum of all even numbers in a Fibonacci sequence
#     up to the maximum value m (non-inclusive of m)."""
    
#     a, b, evens_sum = 0, 1, 0

#     while (a + b) < m:
#         if (a + b) % 2 == 0:
#             evens_sum += (a + b)

#         a, b = b, (a + b)

#     return evens_sum


# Reviewed below. Note that variables can be assigned simultaneously. e.g. a, b = b, a + b
def even_fibb(m):
    a, b = 0, 1
    evens_sum = 0

    while (a+b) < m:
        if  (a + b) % 2 == 0:
            evens_sum += (a + b)
        a, b = b, a + b
    print(evens_sum)

even_fibb(33)