from utils.statistics import *
from utils.reader import *
from pathlib import Path

file_path = Path("data") / "measurements.txt"

print(Path.cwd())

def main():
    if file_path.exists():
        lst = read_numbers(file_path)

        print(calculate_average(lst))
        print(find_max(lst))
        print(find_min(lst))
    else:
        print('Файла не существует')

if __name__ == "__main__": 
    main()

Path("logs").mkdir(exist_ok=True)
