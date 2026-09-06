PASS_MARKS = 40


def calculate_average(marks):
    return sum(marks) / len(marks)

def is_pass(marks):
    if calculate_average(marks) >= PASS_MARKS:
        return True
    else:
        return False

