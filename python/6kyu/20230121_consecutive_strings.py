# 6kyu You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# My ideas:
# Need to find the length of the strings
# Need to see which sum n of consecutive strings is the longest
# Then need to concatenate those longest strings
# I could make another list with the len of all of the strings
# Then use the index of that list to get the index of the word list
# so that I can use the word list to concatenate.

def longest_consec(strarr, k):
    len_list = []
    k_sum = []
    max_sum = 0
    cat_word = ""
    if k > 0:
        for word in strarr:
            len_list.append(len(word))
        for i in range(len(len_list)):
            if i+ k < len(len_list)+1:
                tot_sum = sum(len_list[i:i+k])
                k_sum.append(tot_sum)
                if tot_sum > max_sum:
                    max_sum = tot_sum
                    cat_word = "".join(strarr[i:i+k])
    print(len_list)
    print(k_sum)
    print(max_sum)
    return cat_word

# Refactor:
def longest_consec(strarr, k):
    max_sum = 0
    cat_word = ""
    if k > 0:
        for i in range(len(strarr)):
            if i+ k < len(strarr)+1:
                tot_sum = len("".join(strarr[i:i+k]))
                if tot_sum > max_sum:
                    max_sum = tot_sum
                    cat_word = "".join(strarr[i:i+k])
    print(max_sum)
    return cat_word

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

# Codewars best practice solution:
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result