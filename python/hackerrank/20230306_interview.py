# input -> strings, always lowercase, no numbers or special characters
# output -> shortest string where the first and second strings are overlapping.
# abaaa and aaacc -> abaaacc
# aha and bcb -> ahabbcb

def merge_strings(first, second):
    new_string = first
    # check if the last char of the first word, and first word of the last word are the same 
    for i in range(1, len(first)):
        if first[-i] != second[i-1]:
            new_string += second[i-1:]
        else:
            continue
    
    return new_string

first = 'abcc'
second = "ccss"
merge_strings(first, second)