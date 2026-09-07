def filter_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


def filter_odd(numbers):
    odds = []
    for num in numbers:
        if num % 2 == 1:
            odds.append(num)
    return odds


def filter_above_average(numbers):
    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    above_average = []
    
    for num1 in numbers:
        if num1 > average:
            above_average.append(num1)
    return above_average