def add(x,y):
    return (x+y)

"""
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        i = 2
        last_product = 1
        while i <= n:
            product = i * last_product
            last_product = product
            i += 1
        return product
"""

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        product = 1
        for i in range(1, n+1):
            product *= i
        return product

def sin(x,N):
    sum = 0
    for n in range(N+1):
        sum += ((-1)**n * x**(2*n + 1))/(factorial(2*n + 1))
    return sum

def divide(x,y):
    return (x/y)

def multiply(x,y):
    return x*y

def cos(x,N):
    sum = 0
    for n in range(N+1):
        sum += ((-1)**n * x**(2*n))/(factorial(2*n))
    return sum
    
