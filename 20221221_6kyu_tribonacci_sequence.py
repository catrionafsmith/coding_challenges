# 6kyu Tribonacci sequence
# starting with 3 numbers, return the first n numbers, including those three.

def tribonacci(signature, n):
    new_list = signature
    if n < 3:
        return new_list[:n]
    for i in range(3, n):
        new_list.append(new_list[i-1] + new_list[i-2] + new_list[i-3])
    return new_list

# refactored:
def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    for i in range(3, n):
        signature.append(signature[i-1] + signature[i-2] + signature[i-3])
    return signature

# Best from Codewars:
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

if __name__ == "__main__":
    print(tribonacci([1, 1, 1], 10))
    print((tribonacci([0, 0, 0], 10)))
    # , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(tribonacci([1, 2, 3], 10))
    # , [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
# test.assert_equals# , [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]))