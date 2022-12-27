# 5kyu This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


def zero():
    return 0
def one(): #your code here
    return 1
def two(): #your code here
    return 2
def three(): #your code here
    return 3
def four(): #your code here
    return 4
def five(): #your code here
    return 5
def six(): #your code here
    return 6
def seven(s): #your code here
    if s==minus(s):
        numplus = 7 - s
        return numplus
    elif s==plus(s):
        numminus = 7 + s
        return numminus
    elif s==times(s):
        numtim = 7 * s
        return numtim
    elif "divided_by" in str(s):
        return (7 / s)
    else:
        pass
        # return 7
def eight(): #your code here
    return 8
def nine(): #your code here
    return 9

def plus(s): 
    return s
def minus(s): #your code here
    minit = -s
    return minit 
def times(s): #your code here
    tim = s
    return tim 
def divided_by(s): #your code here
    pass

print(seven(plus(five())))
print(seven(minus(five())))
print(seven(times(five())))
# print(seven(divided_by(five())))

