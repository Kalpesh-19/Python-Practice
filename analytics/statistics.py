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


def calculate_median(numbers):
    numbers = sorted(numbers)

    n = len(numbers)

    if n % 2 != 0:
        return numbers[n // 2]

    return (numbers[n // 2 - 1] + numbers[n // 2]) / 2