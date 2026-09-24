from utils.statistics import *
from utils.reader import *
from pathlib import Path
import logging
import json

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
    input_file = Path(config["input_file"])
    log_file = Path(config['log_file'])

def main():
    
    log_file.parent.mkdir(exist_ok=True)

    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logging.info('Программа запущена')

    
    file_path = input_file
    

    if file_path.exists():
        try:
            lst = read_numbers(file_path)
            logging.info('Файл успешно прочтен')
            logging.info('Значений прочтено: %s', len(lst))
        except ValueError:
            print('В файле не только числа')
            logging.error('В файле не только числа')
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
        logging.error('Файла не существует')

    print(Path.cwd())

    logging.info('Конец программы')
if __name__ == "__main__": 
    main()


