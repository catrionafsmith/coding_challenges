# 7kyu An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# My ideas:
# create a list and iterate through the string, checking to see if each letter is in the list. (Then add it to the list)
# check if each letter is in the string made up of the rest of the string - use slicing to check.


# Initial solution
def is_isogram(string):
    used_letters = []
    for letter in string:
        if letter.lower() in used_letters:
            return False
        else:
            used_letters.append(letter.lower())
    return True

# struggling to refactor as I'm not sure how to refer to 'what remains of the string after I have looked at one letter

def is_isogram(string):
    used_letters = []
    for letter in string if letter.lower() in string[]:
        
            return False
        else:
            used_letters.append(letter.lower())
    return ''.join(for letter in string if letter.lower() in )

# Best solution from Codewars:
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# (set(string.lower())) means how many unique objects are there?
