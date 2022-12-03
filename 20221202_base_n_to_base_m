# Converting a number in any base to base 10:
numb10 = 0
number = "a3"
from_base = 13
# for n in range(len(number)):
#     numb10 += (int(number[len(number)-(1+n)]))*(from_base**n)
b_digits = "0123456789abcdefghijklmnopqrstuvwxyz"

# need to get the index from b_digits for values >9:
for n in range(len(number)):
    numb10 += (b_digits.index(number[len(number)-(1+n)]))*(from_base**n)
print(numb10)




# Trying to figure out how to convert a number to another base:
base = 8
numb10 = 133
numb_n = ""
quotient = numb10
while quotient > 0:
    numb_n = str(quotient % base) + numb_n
    quotient = numb10//base
    numb10 = quotient
print(numb_n)

# Then make sure that the number uses abcdefghijklmn... if the required digit is higher than 10.
base = 13
numb10 = 133
numb_n = ""
quotient = numb10
b_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
while quotient > 0:
    numb_n = b_digits[(quotient % base)] + numb_n
    quotient = numb10//base
    numb10 = quotient
print(numb_n)

# check how many times digits d is found in string numb_n
print(numb_n.count("a"))

def count_digit(number, digit, base=10, from_base=10):
    numb10 = 0
    b_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    for n in range(len(number)):
        numb10 += (b_digits.index(number[len(number)-(1+n)]))*(from_base**n)
    numb_n = ""
    quotient = numb10
    while quotient > 0:
        numb_n = b_digits[(quotient % base)] + numb_n
        quotient = numb10//base
        numb10 = quotient
    print(numb_n.count(digit))
    print(type(numb_n))
    print(type(digit))
    print(numb_n == digit)
    print(numb_n)
    return numb_n.count(digit)

count_digit("0","0")

# Solution:
# numb_n was an empty string, so if numb10 = 0, numb_n = "0"

# My full solution
def count_digit(number, digit, base=10, from_base=10):
    numb10 = 0
    b_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    for n in range(len(number)):
        numb10 += (b_digits.index(number[len(number)-(1+n)]))*(from_base**n)
    numb_n = ""
    if numb10 == 0:
        numb_n = "0"
    quotient = numb10
    while quotient > 0:
        numb_n = b_digits[(quotient % base)] + numb_n
        quotient = numb10//base
        numb10 = quotient
    return numb_n.count(digit)

# Other solutions from Codewars:
def count_digit(number, digit, base=10, from_base=10):
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    f = lambda x: a[x] if x<base else f(x//base) + a[x%base]
    return f(int(number, from_base)).count(digit)