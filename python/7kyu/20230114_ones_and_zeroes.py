# 7kyu 

# My ideas:
# reverse the array  
# then multiply each array value by its decimal value

def binary_array_to_number(arr):
    r_arr = arr.reverse()
    print(arr)
    bin_tot = 0
    if r_arr != None:
        for i in range(len(r_arr)):
            # print(r_arr[i])
            # print(2**i)
            bin_tot += r_arr[i]*(2^i)
    print(bin_tot)
    return bin_tot

binary_array_to_number([0,0,0,1])