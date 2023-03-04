def mergeLists(head1, head2):
    i = 0
    j = 0
    merged_list = []
    # Move the slider i along the values of head1 comparing them with head2 and adding the lower value while there are values in BOTH lists
    # Append the lower value to the list
    # Move the slider along after each comparison
    # Continue the comparison until one list is finished
    while i < len(head1) and j <len(head2):
        if head1[i] < head2[j]:
            merged_list.append(head1[i])
            i += 1
        elif head1[i] == head2[j]:
            merged_list.append(head1[i])
            merged_list.append(head2[j])
            i += 1
            j += 1
        else: #head2 is less than head1
            merged_list.append(head2[j])
            j += 1
    # When one list is finished, append the rest of the other list to merged_list
    if i == len(head1):
        for m in range(j, len(head2)):
            merged_list.append(head2[m])
    elif j == len(head2):
        for n in range(i, len(head1)):
            merged_list.append(head1[n])
    
    return merged_list
           
head1 = [1, 3, 7]
head2 = [1, 2]

print(mergeLists(head1, head2))