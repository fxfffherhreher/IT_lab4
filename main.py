from utils.statistics import *
from utils.reader import *
from pathlib import Path


def main():
    try:
        file_path = Path("data") / "measurements.txt"
    except FileNotFoundError:
        print('Файла не существует')

    if file_path.exists():
        try:
            lst = read_numbers(file_path)

            print(calculate_average(lst))
            print(find_max(lst))
            print(find_min(lst))
        except ValueError:
            print('В файле не только числа')
    
    else:
        print('Файла не существует')

    print(Path.cwd())

    Path("logs").mkdir(exist_ok=True)

if __name__ == "__main__": 
    main()


