#  6kyu Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.

# My ideas:
# I need to calculate what each digit to the power of p and successive numbers is.
# I could do that by changing the main number to a string, taking each digit indivdually and then changing it back to a number to multiply it by p etc.
# Then to check if there is an integer that is a divisor of the main number, 
# we just need to do sum(exponent)%main argument, and if it is zero then return sum(exponent)%main argument if false return -1

def dig_pow(n, p):
    sum_exp = 0
    str_n = str(n)
    for i in range(len(str_n)):
        sum_exp += int(str_n[i])**(p+i)    
    if sum_exp % n == 0:
        return sum_exp // n
    else:
        return -1


print(dig_pow(46288, 3))

# Best Practice from CodeWars - using the enumerate function which creates an indexed list for an item:
# This also uses the pow() function
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

# Similar version but without pow()
def dig_pow(n, p):
  t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
  return t//n if t%n==0 else -1

