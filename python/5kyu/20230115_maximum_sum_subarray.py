# 5kyuThe maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray. 

# My ideas:



# def max_sequence(arr):
#     max_tot = 0
#     sum_num = 0
#     for num in arr:
#         sum_num += num
#         if sum_num > max_tot:
#             max_tot = sum_num 
#     return max_tot

# def max_sequence(arr):
#     max_tot = 0
    
#     for i in range(len(arr)):
#         sum_num = 0
#         for i in range(len(arr)):
#             sum_num += arr[i]
#             print(f"for {arr[i]}")
#             print(f"This is the sum_num {sum_num}")
#             if sum_num > max_tot:
#                 max_tot = sum_num 
#     return max_tot

# def max_sequence(arr):
#     max_tot = 0
#     k = 0 
#     l = 0
#     for num in arr[k:len(arr)-l]:
#         sum_num = 0
#         for num in arr[k:len(arr)-l]:
#             sum_num = sum(arr[k:len(arr)-l])
#             print(f"for {num}")
#             print(f"This is the sum_num {sum_num}")
#             print(k)
#             print(l)
#             if sum_num > max_tot:
#                 max_tot = sum_num 
#             l +=1
#         print("Hi")
#         k+=1
#     return max_tot

def max_sequence(arr):
    max_tot = 0
    k = 0 
    for i in range(len(arr)):
        sum_num = 0
        for num in arr[k:]:
            sum_num += num
            print(sum_num)
            if sum_num > max_tot:
                max_tot = sum_num 
        k += 1

    print(f"This is max {max_tot}")
    return max_tot

# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))