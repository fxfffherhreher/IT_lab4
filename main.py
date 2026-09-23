from utils.statistics import *
from utils.reader import *
from pathlib import Path


def main():
    file_path = Path("data") / "measurements.txt"
    if file_path.exists():
        lst = read_numbers(file_path)

        print(calculate_average(lst))
        print(find_max(lst))
        print(find_min(lst))
    else:
        print('Файла не существует')

    print(Path.cwd())

    Path("logs").mkdir(exist_ok=True)

if __name__ == "__main__": 
    main()


