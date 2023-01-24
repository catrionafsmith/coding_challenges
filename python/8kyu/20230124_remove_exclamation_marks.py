#  8kyu Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

# My ideas:
# Could use a for loop and remove(char) if char == "!"
# *as remove("!") would only remove the first instance of !
# could use a regex and remove "!" /g (globally)
# *because strings are immutable, I would need to start a new string anyway

def remove_exclamation_marks(s):
    new_str = ""
    for char in s:
        if char != "!":
            new_str += char
    return new_str

# Refactored
def remove_exclamation_marks(s):
    return ''.join(char for char in s if char != "!")


# Best solution from Codewars:
# using replace()
def remove_exclamation_marks(s):
    return s.replace('!', '')