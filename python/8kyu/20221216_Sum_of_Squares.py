# 8kyu Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.


def square_sum(numbers):
    sum_sq = 0
    for i in numbers:
        sum_sq += i*i
    return sum_sq

# from Codewars - best solution:
def square_sum(numbers):
    return sum(n**2 for n in numbers)

if __name__ == "__main__":
    numbers = [1, 2, 2]
    print(square_sum(numbers))
