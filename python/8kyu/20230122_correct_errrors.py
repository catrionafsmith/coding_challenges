#  8kyu Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

# My ideas:
# 
# Use a for loop
#  Replace the required letters

def correct(s):
    new_str = ""
    for char in s:
        if char == "5":
            new_str += "S"
        elif char == "0":
            new_str += "O"
        elif char == "1":
            new_str += "I"
        else:
            new_str += char
    return new_str

print(correct("PAR15"))

# Codewars best practice:
def correct(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5','S')