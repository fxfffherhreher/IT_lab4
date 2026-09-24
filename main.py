from utils.statistics import *
from utils.reader import *
from pathlib import Path
import logging


def main():
    Path("logs").mkdir(exist_ok=True)
    
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logging.info('Программа запущена')

    try:
        file_path = Path("data") / "measurements.txt"
    except FileNotFoundError:
        logging.ERROR('Файла не существует')
        print('Файла не существует')

    if file_path.exists():
        try:
            lst = read_numbers(file_path)
            logging.info('Файл успешно прочтен')
            logging.info('Значений прочтено: %s', len(lst))
        except ValueError:
            print('В файле не только числа')
            logging.ERROR('В файле не только числа')
        try:
            validate_numbers(lst)
            print(calculate_average(lst))
            print(find_max(lst))
            print(find_min(lst))
        except ValueError as e:
            print(e)
            logging.error('Список измерений пуст')

        
    else:
        print('Файла не существует')

    print(Path.cwd())

    logging.info('Конец программы')
if __name__ == "__main__": 
    main()


