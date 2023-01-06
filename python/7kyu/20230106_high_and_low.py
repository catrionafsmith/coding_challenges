# 7kyu DESCRIPTION:
# In this little assignment you are given a string of space 
# separated numbers, and have to return the highest and lowest number.

# My ideas - space separated, so use split()
# use max and min functions
# use an f-string to return

def high_and_low(numbers):
    n = numbers.split()
    int_list = [int(i) for i in n]
    max_n = max(int_list)
    min_n = min(int_list)
    return f"{max_n} {min_n}"

# Refactor:
def high_and_low(numbers):
    n = numbers.split()
    int_list = [int(i) for i in n]
    return f"{max(int_list)} {min(int_list)}"


if __name__ == "__main__":
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# Best solutions from Codewars:
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"

