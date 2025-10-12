def load_strings(filename):
    with open(filename, 'r') as file:
        strings = [line.strip() for line in file if line.strip()]
    return strings  