# 8kyu This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# My ideas:
# Use %2 == 0 to find if a number is even or not.
# Use if else statements

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
# Refactored
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

# Best practices from Codewars:
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8
# Because if number % 2 is True it must have an answer which is not 0

# Clever response:
def simple_multiplication(n):
    return n * (8 + n % 2)