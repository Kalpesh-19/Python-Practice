def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    total = 1
    for num in range(n, 0, -1):
        total *= num
    return total
