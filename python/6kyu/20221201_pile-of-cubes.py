# 6kyu Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n3 n^3n 
# 3
#  , the cube above will have volume of (n−1)3 (n-1)^3(n−1) 
# 3
#   and so on until the top which will have a volume of 13 1^31 
# 3
#  .

# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n3+(n−1)3+(n−2)3+...+13=m n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = mn 
# 3
#  +(n−1) 
# 3
#  +(n−2) 
# 3
#  +...+1 
# 3
#  =m if such a n exists or -1 if there is no such n.

# def find_nb(m):
#     for n in range(m):
#         if ((n**2)-sum(range(n)))**3 == m:
#             print(n)
#             return n
#         else:
#             print(-1)
#             return -1
# find_nb(1071225)

# def find_nb(m):
#     for n in range(m):
#         if (((n-1)*n)/2)**3 == m:
#             print(n)
#             return n
#         else:
#             print(-1)
#             return -1
# find_nb(1071225)

# m=0
# for n in range(46):
#     m += (n)**3
# print(m)
# print(sum(range(46)))
# print(45**2)
# from math import sqrt
# def find_nb(m):
#     for n in range(100):
#         if n*(n**3)-sum((range(n)))**3 == m:
#             print(n)
#             return n
#         else:
#             print(-1)
#             return -1
# find_nb(1071225)

# n = 45
# print((n*(n**3))-(sum((range(n)))**3))

# print(sum(range(6)))
# Make a list using the range
# cube everything in the list
# def find_nb(m):
#     list = 0
#     for n in range(46):
#         list += n**3
#         print(list)
#         if list == m:
#             print(True)
#         else:
#             print("No tru")

# find_nb(1071225)

# Finalised solution
def find_nb(m):
    list = 0
    for n in range(m):
        list += n**3
        if list == m:
            return n
        elif list > m:
            break
    return -1


