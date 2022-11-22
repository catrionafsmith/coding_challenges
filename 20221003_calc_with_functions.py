from tkinter import S


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

