def fiboN(n):
    i = 0
    n1 = 0
    n2 = 1
    while i < n - 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
    return n3

print("The", 5, "th term of the Fibonacci sequence is", fiboN(5))
print("The", 10, "th term of the Fibonacci sequence is", fiboN(10))
print("The", 15, "th term of the Fibonacci sequence is", fiboN(15))
