def load_numbers(filename):
    with open(f"{filename}") as f:
        content = f.read()
    numbers = content.split()

    nums = []
    for num in numbers:
        number = int(num)
        nums.append(number)
    return nums
