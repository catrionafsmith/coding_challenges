# Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
#
# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

# Ideas:
# number of bribes is the difference between index+1 and current index.
# can use index() to get the current index, or they could be mapped or enumerated.
# enumerating can give the index and the value, so maybe that's best.

# def minimumBribes(q):
#     bribes = 0
#     for i, val in enumerate(q):
#         if val > i +3:
#             return "Too chaotic"
#         else:
#             if val-(i+1) > 0:
#                 bribes += (val - (i+1))
#     return bribes

def minimumBribes(q):
    if len(q) > 1:# initialise bribes as 0
        bribes = 0
        # enumerate q
        for i, val in enumerate(q):
            # if the value is greater than index +2 they have bribed too many people
            if val > i +3:
                return "Too chaotic"
            else:
                # if they have bribed at least one person, their value will be greater than index+1.
                if val-(i+1) > 0:
                    bribes += (val - (i+1))
        # return the number of bribes
        return bribes

q = [1, 2, 5, 3, 7, 8, 6, 4]
i = [1, 2, 3, 4, 5, 6, 7, 8]
print(minimumBribes(q))