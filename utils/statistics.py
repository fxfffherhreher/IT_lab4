def calculate_sum(numbers):
    sm = 0
    for elem in numbers:
        sm += elem
    return sm

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

def find_min(numbers):
    mn = float('inf')
    for elem in numbers:
        if elem < mn:
            mn = elem
    return mn

def find_max(numbers):
    mx = -float('inf')
    for elem in numbers:
        if elem > mx:
            mx = elem
    return mx

