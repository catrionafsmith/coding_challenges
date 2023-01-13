# 6kyu

# My ideas:
# Split the sentence on spaces
# Find the digits in each word
# Assign the digits to be the index of the word in the output sentence
import string

def order(sentence):
    sentence = sentence.split()
    word_list = [0]*len(sentence)
    # print(word_list)
    for word in sentence:
        for char in word:
            if char in string.digits:
                pass
                word_list[int(char)-1] = word
    return " ".join(word_list)





print(order("is2 Thi1s T4est 3a"))