
#6A

def is_even(n):
    if n % 2 == 0:
        answer = True
    else:
        answer = False
    return answer

print(is_even(0))

#6B

def classify_triangle(a,b,c):
    if a == b == c:
        result = "equilateral"
    elif a == b or a == c or b == c:
        result = "isosceles"
    else:
        result = "scalene"
    return result

print(classify_triangle(5,5,5))
print(classify_triangle(5,3,5))
print(classify_triangle(5,4,1))
