# 7kyu Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.


def reverse_words(text):
    new_string = ""
    new_list = text.split()
    sp_count = (text.count(' '))
    print(sp_count)
    len_new_list = len(new_list)
    print(len_new_list)
    for word in new_list:
        new_string += word[::-1] + (" "*int((sp_count/(len_new_list-1))))
    return new_string.strip()

if __name__ == "__main__":
    # print(reverse_words('The quick brown fox jumps over the lazy dog.'))
    # # print(reverse_words('apple'))
    # print(reverse_words('a b c d'))
    # print(reverse_words('double  spaced  words'))

# Best result from codewars:
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))