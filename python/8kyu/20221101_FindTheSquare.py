def is_square(n):
    for i in range(n+1):
        print(i)
        print(n)
        if i*i == n:
            return True
        else:
            return False

is_square(4)
