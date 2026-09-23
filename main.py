from utils.statistics import *
from utils.reader import *
from pathlib import Path


def main():
    lst = read_numbers('data/measurements.txt')

    print(calculate_average(lst))
    print(find_max(lst))
    print(find_min(lst))

if __name__ == "__main__": 
    main()