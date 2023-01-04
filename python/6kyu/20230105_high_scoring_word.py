# 6kyu:
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

# Initial ideas:
# Split string of words into a list using split.
# Each letter scores points based on the position in alphabet - the same as the index of the letter
# or could use comparison operators to compare letters
# return the highest scoring word as a string - cycle through the words, and store the highest scoring as a 'max'
# look for index of word in the alphabet.

def high(x):
    words = x.split()
    alpha = "*abcdefghijklmnopqrstuvwxyz"
    max_score = 0
    max_word = ""
    for word in words:
        tot_score = 0
        for letter in word:
            tot_score += int((alpha.index(letter)))
            if tot_score > max_score:
                max_score = tot_score
                max_word = word
    return max_word


if __name__ == "__main__":
    high('man i need a taxi up to ubud')

# Best from Codewars:
def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

# New learning: ord()
# The ord() function returns the number representing the unicode code of a specified character.