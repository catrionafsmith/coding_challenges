def find_short(s):
#     set a variable to represent shortest word
    short_length = len(s)
    # split string on space
    split_str = s.split()
#     cycle through and find the length of each
    for i in range(len(split_str)):
        len_word = len(split_str[i])
        if len_word < short_length:
            short_length = len_word
# find the shortest word (smallest length)

# return len shortest word
    return short_length

print(find_short('hi there'))