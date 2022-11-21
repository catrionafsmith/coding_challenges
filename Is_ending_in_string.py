# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).


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

#Best solution
def solution(string, ending):
    return string.endswith(ending)

#or
def solution(string, ending):
    return ending in string[-len(ending):]