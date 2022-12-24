# 7kyu Count the error letters
# in a string, count the errors letters (those outwith a-m)
# and return the number of errors over the length of the string

# First ideas:
# Need to count the number of letters which are outwith a-m.
# use count function?
# could use regex for letters in a group?

# First example:
def printer_error(s):
    good_let = "abcdefghijklm"
    count_bad = 0
    for letter in s:
        if not letter in good_let:
            count_bad += 1
    error_rate = f"{count_bad}/{len(s)}"
    return error_rate 

# Refactor:
def printer_error(s):
    good_let = "abcdefghijklm"
    count_bad = 0
    for letter in s:
        if not letter in good_let:
            count_bad += 1
    return f"{count_bad}/{len(s)}"

# Good examples from codewars:
# can use the format() method to put the length of the error and the string into a fraction format.
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
   
# or
# because > works with letters too
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count) 