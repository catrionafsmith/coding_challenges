# We define super digit of an integer  using the following rules:
#
# Given an integer, we need to find the super digit of the integer.
#
# If  has only  digit, then its super digit is .
# Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
# For example, the super digit of 9875 will be calculated as:
#
# 	super_digit(9875)   	9+8+7+5 = 29
# 	super_digit(29) 	2 + 9 = 11
# 	super_digit(11)		1 + 1 = 2
# 	super_digit(2)		= 2

# The number p is created by concatenating the string n, k times.

# Ideas:
# If the number produced when Superdigit is called is greater than 10, then superdigit is called again
# superdigit could convert to string and back again to use each digit in turn.

def superDigit(n: str, k: int) -> int:
#     # Create number p, from number n, concatenated k times (convert n to string):
    p = (n)*k
    tot = 0
    list_of_numbers =[]
    list_of_numbers = list(map(int, p.strip()))
    tot = sum(list_of_numbers)
    if tot < 10:
        return tot
    else:
        return superDigit(str(tot), 1)

def superDigit(n: str, k: int) -> int:
#     # Create number p, from number n, concatenated k times (convert n to string):
    p = (n)*k
    tot = 0
    list_of_numbers =[]
    list_of_numbers = list(map(int, p.strip()))
    tot = sum(list_of_numbers)
    if tot < 10:
        return tot
    else:
        return tot%9


# to solve super digit
# def superDigit(n: str, k: int) -> int:
#     # Create number p, from number n, concatenated k times (convert n to string):
#     p = int((n)*k)
#     # total_sum = 0
#     # convert p to a string, or a list
#     def sumdig(num):
#         list_num = [int(x) for x in str(num)]
#         global total_sum
#         total_sum = sum(list_num)
#         while total_sum > 10:
#             sumdig(total_sum)
#         return total_sum
#
#     sumdig(p)
#
#     return total_sum
# def sumdig(num):
#     list_num = 0
#     for i, n in enumerate(str(num)):
#         list_num += int(n)
#
#     while list_num >= 10:
#         list_num = sumdig(list_num)
#     return list_num
#
# def superDigit(n: str, k: int) -> int:
#     # Create number p, from number n, concatenated k times (convert n to string):
#     p = int((n)*k)
#     # total_sum = 0
#     # convert p to a string, or a list
#
#     tot = sumdig(p)
#
#     return tot


# def superDigit(n: str) -> int:
#     """
#
#
#     """



    # in order to add all digits.
    # if the result has more than two digits (is greater than 10), then repeat the process of adding the digits
    # When the result is less than 10, return that result (the super digit)


print(superDigit("148", 3))
