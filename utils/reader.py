def read_numbers(file_path):
    with open(file_path) as f:
        ans = [float(x) for x in f]

    return ans