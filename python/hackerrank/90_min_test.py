# 4th bit

# def dec_to_bin(num):
#     bin_str = ""
#     remainder = 0
#     while num > 0:
#         remainder = num % 2
#         bin_str += str(remainder)
#         num = num // 2
#     return bin_str[::-1]

# or
def dec_to_bin(num):
    binary_num = bin(num)
    return binary_num[-4]

num = 23
# print(dec_to_bin(num))

# No Pairs Allowed
def no_pairs(words):
    # make variables for sam_let and rep_char
    # check each word to see if there are two letters the same next to each other
    # if there are two letters the same, the replace_score is 1
    # if there are three letters in a row the same, the replace score is 1
    # if there are four letters in a row the same, the replace score is 2
    # 5 letters 2
    #  6 letters 3
    # so the number of letters the same is sam_let, replace score is int(sam_let//2)
    # sam let and int replace score are reset to zero when a new word starts.
    replace_array = []
    for str in words:
        # Start with sam_let as 1, because if two letters are the same, then 1 will be added (so the value of sam_let = = the number of characters that are the same)
        sam_let = 1
        rep_char = 0
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                sam_let += 1
        replace_array.append(int(sam_let//2))
    return replace_array

words = ['aab', 'aba', 'boook', 'aaaaaa']
# print(no_pairs(words))

# All Characters in a string
import string
def check_allchars(sentences):
#     check each string in sentences to see if it contains all of the characters in the alphabet
# use set(string) to see how many unique chars are in each string
# can use the string module to import the lowercase strings and check that the set of lowercase ASCII chars is in the strings set.
    for i in range(len(sentences)):
        if set(string.ascii_lowercase) <= set(sentences[i]):
            # Here we are directly altering the list supplied as a parameter, which is sometimes inadvisable
            sentences[i] = 1
        else:
            sentences[i] = 0
    return sentences

sentences = ['aab', 'aba', 'Abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','the quick brown fox jumps over the next lazy dog']
# print(check_allchars(sentences))

# Group Transactions
# def shopping_list(transactions):
    # for each item in the list I need to note its frequency/count
    #  I need to order the items in descending order of frequency
    #  and alphabetically for items that have the same frequency
    # then I return the transactions as a new array, where each item is the "item count"

    # To get the frequency i could use count()
    # Or I could have a counter
    # I could put the items into separate arrays based on their count, alphabetically sort them, then put them into another array
    # trans_dict = {}
    # counted = []
    # for item in transactions:
    #     if item not in counted:
    #         trans_dict[f"{item} {transactions.count(item)}"] = transactions.count(item)
    #         counted.append(item)
    # print(trans_dict)
    # n_trans_dict = (sorted(trans_dict))
    # print(n_trans_dict)
    # sort_trans = sorted(n_trans_dict.items(), key=lambda x: x[1], reverse=True)
    # print(sort_trans)
    # for i in sort_trans:
    #     print(i[0])
    # print(sorted(trans_lists, reverse = True))


# transactions = ("bin", "bin", "bin", "potato", "potato", "apple", "apple", "cheese","apple")
# shopping_list(transactions)

def dec_to_bin(num):
    rem = 0
    rev_bin = ""
    while num > 0:
        rem = num % 2 
        num = num //2
        rev_bin += str(rem)
    bin = rev_bin[::-1]
    return bin[-4]

num = 23
# print(dec_to_bin(23))


# def no_same_let(words):
#     return_array = []
#     for j in range(len(words)):
#         same_let = 1
#         for i in range(len(words[j])-1):
#             if words[j][i+1] == words[j][i]:
#                 same_let += 1
#         return_array.append(same_let//2)
#     return return_array

def no_same_let(words):
    return_array = []
    for word in words:
        same_let = 1
        for i in range(len(word)-1):
            if word[i+1] == word[i]:
                same_let += 1
        return_array.append(same_let//2)
    return return_array

words = ["boom", "boook", "no"]
print(no_same_let(words))

def all_char(string_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return_array2 = []
    for word in string_list:
        word2 = word.replace(" ", "")
        if set(word2) == set(alphabet):
            return_array2.append(1)
        else:
            return_array2.append(0)
    return return_array2

sentences = ['aab', 'aba', ' abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','the quick brown fox jumps over the next lazy dog']
print(all_char(sentences))