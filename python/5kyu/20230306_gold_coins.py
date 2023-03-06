def number_of_coins(info):
    """
    Return the minimum number of gold coins given the guardian info
    while i > -1:
    iterate through list of tuples
    for each tuple we create a condition that mystery % mN will = aN
    if i fails any conditions then i+=1
    return i
    """
    i = 0
    for i in len(info):
        for (a, m) in info:
            if i % m != a:
                i += 1
    return i
    
print(number_of_coins([(1, 2), (2, 5)]))