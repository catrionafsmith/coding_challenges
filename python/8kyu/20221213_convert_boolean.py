# 8kyu Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

# is there a way to do it with a ternary operator?
# incorrect syntax
# def bool_to_word(boolean):
#     boolean == True ? return "Yes" : return "No"

# correct ternary syntax for python
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"

# Alternative from Codewars:
def bool_to_word(bool):
    if bool:
        return "Yes"
    return "No" 