# 7kyu def make backronym An acronym deliberately formed from a phrase whose initial letters spell out a particular word or words, either to create a memorable name or as a fanciful explanation of a word's origin.

# "Biodiversity Serving Our Nation", or BISON

# My ideas:
# words come from pre-loaded dictionary. Initials are keys in the dictionary
# Loop through the acronym and get the value for each initial and add it to a string or a list
# If words are added to a list then join the list.

#preloaded variable: "dictionary"
def make_backronym(acronym):
    new_ac = ""
    for char in acronym:
        new_ac += dictionary[char]

    return new_ac
# This solution either doesn't include spaces, or if I add a space each time then there is a trailing space.

# Solution 2:
def make_backronym(acronym):
    new_ac = []
    for char in acronym:
        new_ac.append(dictionary[char.upper()])
    return " ".join(new_ac)

# Codewars best practice:
def make_backronym(acronym):
    return ' '.join(dictionary[char.upper()] for char in acronym)
