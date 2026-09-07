def load_numbers(filename):
    with open(f"{filename}") as f:
        content = f.read()
    word = content.split()
    return word
