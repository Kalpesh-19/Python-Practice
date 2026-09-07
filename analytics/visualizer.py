def print_bar_chart(numbers):
    for num in numbers:
        x = "*"
        print(f"{num} | {"*" * num}")


print_bar_chart([10, 20, 30])