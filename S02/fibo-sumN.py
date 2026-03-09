def fibosum(n):
    i = 0
    n1 = 0
    n2 = 1
    res = 1
    while i < n - 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
        res += n3
    return res

print("The sum of the first", 5, "terms of the Fibonacci sequence is", fibosum(5))
print("The sum of the first", 10, "terms of the Fibonacci sequence is", fibosum(10))