# 7kyu Your task is to write a function which returns the sum of following series upto nth term(parameter).

# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# My ideas:
# Need to round the answer to two decimal places, and return it a a string:
# Will need to use :2f in the f-string, and make sure that it is a string output.
# What is the series?
# 1/1, 1/4, 1/7, 1/10, 1/13 (plus 3 each time on the denominator)

# def series_sum(n):
#     sum_num = 0
#     for i in range(1, n, 3):
#         sum_num += 1/i
#         print(sum_num)
#     return f"{sum_num:2f}"

# print(series_sum(3))

def series_sum(n):
    sum_num = 0
    for i in range(1, (n*3)-1, 3):
        sum_num += 1/(i)
    return f"{(sum_num):.2f}"

print(series_sum(5))

# Best answers in codewars:
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
