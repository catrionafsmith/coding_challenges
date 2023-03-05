def truckTour(petrolpumps):
    # Write your code here
    # receives a 2D array
    # first number is the amount of petrol it gives
    # second number is the distance to the next pump
    # need to return the smallest index of the pump that we can start from and complete the circle.
    # each km that we travel we will consume 1 litre of petrol.
    # for each row in petrol pumps, need to see if element 1 is greater than element 2.
    # Can I use mapping to add the elements?
    # Need to make sure that it goes through all the rows. Do I need to reset the
    sum_ele1 = 0
    sum_ele2 = 0
    i = 0
    while i < j:
        for j in range (len(petrolpumps)):
            sum_ele1 += petrolpumps[i][0]
            sum_ele2 += petrolpumps[i][1]
            if sum_ele1 < sum_ele2:
                sum_ele1 = 0
                sum_ele2 = 0
                i +=1
            else:
                i+=1
                continue

    # if element 2 is greater than sum 1, break and try next row.
    # if element 1 is greater than element 2, continue on to next line and continue to add element 1 for row 2 on to elemnt 1 for row 1. the same for element 2. again if element2 sum is greater than element1 sum, break
    # if we are able to get all the way to the last row, make sure that we go back up to the top and continue to add all of the other rows until we have added all.
    # if we are able to add all rows, return the index of the row.

petrolpumps = [[1,5],[10, 3],[3, 4]]
truckTour(petrolpumps)