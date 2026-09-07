def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum