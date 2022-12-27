#  8kyu Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# My ideas:
# Does Python have an 'atIndex' function?

def findNeedle(haystack):
    needle_find = haystack.index("needle")
    print(f"found the needle at position {needle_find}")

hay = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
findNeedle(hay)

# reformatted 
def find_needle(haystack):
    return(f"found the needle at position {haystack.index('needle')}")

# from looking at Codewars solutions:
# brackets not needed for return function