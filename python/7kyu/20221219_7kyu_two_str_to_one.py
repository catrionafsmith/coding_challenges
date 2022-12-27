#  7kyu

def longest(a1, a2):
    a3 = []
#     s3 = a1.split("")
#     s3.append(a2.split(""))
    for letter in a1:
        if letter not in a3:
            a3.append(letter)
    for letter in a2:
        if letter not in a3:
            a3.append(letter)
    print(a3)
    sorted_list = sorted(a3)
    print(sorted_list)
    joined_str = "".join(sorted(a3))
    print(joined_str)
 return joined_str

# Refactored:
def longest(a1, a2):
    a3 = []
    for letter in a1:
        if letter not in a3:
            a3.append(letter)
    for letter in a2:
        if letter not in a3:
            a3.append(letter)
    joined_str = "".join(sorted(a3))
    return joined_str

# Marginally shorter:
def longest(a1, a2):
    a3 = []
    a4 = a1 + a2
    for letter in a4:
        if letter not in a3:
            a3.append(letter)
    return "".join(sorted(a3))

# Possibly structure of a shorter solutions
return "".join(sorted(x) for x in a1, a2)

# Best solution from CodeWars - N.B. sets are immutable but you can add to them.
# Sorted creates a new copy of the listed data.
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


if __name__ == "__main__":
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a, b)