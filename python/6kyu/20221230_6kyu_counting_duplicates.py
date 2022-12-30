#6kyu Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# My ideas:
# Use set to find number of individual characters, then subtract from len(string)?
# Make a string with repeated letters and then check the length of it.

# set wont work, as that gives a higher answer if a lingle letter is repeated.
# def duplicate_count(text):
#     return len(text) - len(set(text.lower()))
# count of letters - if count is greater than 1 it doesn't matter.

def duplicate_count(text):
    repeated_letter = ""
    count = 0
    for i in range(len(text)):
        if text[i].lower() in repeated_letter:
            count += 1
            repeated_letter += text[i].lower()
    print(count)
    return count

def duplicate_count(text):
    repeated_letter = ""
    text = text.lower()
    count = 0
    for i in range(len(text)):
        if text.count(text[i]) > 1 and not text[i] in repeated_letter:
            count += 1
            repeated_letter += text[i]
        else:
            repeated_letter += text[i]
    return count

(duplicate_count("abcdeaB"))

# Best codewar solution:
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
     