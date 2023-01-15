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

# Best results from Codewars:
def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our sentence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)



print(order("is2 Thi1s T4est 3a"))