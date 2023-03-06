# In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.
# Create the sequence to the first n numbers.
# each number should be added to an array as it is created.

def fib_seq(n):
    # find length of n
    # start the sequence from 0 or [0, 1]
    # continue seq by adding two prev digits.
    # continue until list has n items in it.
    fib_list = [0, 1]
    for i in range(n-2):
        new_dig = fib_list[i] + fib_list[i+1]
        fib_list.append(new_dig)
    return fib_list

print(fib_seq(10))