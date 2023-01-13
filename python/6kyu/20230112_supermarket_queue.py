# 6kyu There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

# My ideas;
# Make a total for each queue (there will be n queues for n tills).
# Iterate through the customer list, adding to the minimum value queue each time

def queue_time(customers, n):
    queue_list = [0 for i in range(n)]
    print(queue_list)
    for person in customers:
        queue_list[queue_list.index(min(queue_list))] += person
    return max(queue_list)


print(queue_time([1,2,3,4,5], 1))

# Best solutions in Codewars: (Similar to mine but using [0]*n to create a list of n zeros.)
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
