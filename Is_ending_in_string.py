# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

########
# My thoughts:
# Check positions from end - use negative indexes
# Only need to check for len(ending) chars
# Could reverse the strings - would that help? - use a slice that steps backwards string[::-1]


# My solution:
def solution(string, ending):
    if ending == '':
        return True
    if len(ending) > len(string):
        return False
    for n in range(len(ending)):
        if ending[-n-1] == string[-n-1]:
            # Can't do return True here because it wouldn't go through the whole for loop. Need to use continue
            continue
        else:
            return False
        return True

#Best solution - there is a python function endswith (and also startswith)!
def solution(string, ending):
    return string.endswith(ending)

#or checking if the ending is in a string slice, based on the length of the ending. N.B. If the ending is longer than the string
# True will not be returned.
def solution(string, ending):
    return ending in string[-len(ending):]