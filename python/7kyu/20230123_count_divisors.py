# 7kyu Count the number of divisors of a positive integer n.

# My ideas:
# use a loop and check for numbers smaller than n where the modulo is zero.
# for efficiency, I could check for % of 2 then only check for integers up to half of n?

def divisors(n):
    divs = 0
    for i in range(1, n+1):
        if n % i == 0:
            divs +=1
    return divs


# Best practice solution from CodeWars:
def divisors(n):
    return len([i for i in range(1, n+1) if n%i == 0])