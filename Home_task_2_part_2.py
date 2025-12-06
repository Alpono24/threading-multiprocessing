

# Задание 2. Аналогичная задача: три программы, одна
# последовательная, другая поточная, третья процессная. Но они
# занимаются не математикой, а GET-запросами на любые юрлки.
# Итог. По заданию 1 замерить время выполнения всех трех
# программ, сравнить. По заданию 2 тоже замерить и сравнить.
# Сделать выводы

import time
import requests
import logging
import threading

logging.basicConfig(
    filename='Home_task_2_information_about_calculations.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def download_content(url):
    try:
        response= requests.get(url)
        if response.ok:
            logging.info(f"Содержимое {url} имеет размер {len(response.text)} символов")
            return response
        else:
            logging.error(f'Ошибка при загрузке {url}: {response.status_code}')
            return None
    except  requests.RequestException as e:
        logging.error(f'Ошибка при загрузке {url}: {e}')
        return None

urls = [
    'https://www.onliner.by/',
    'https://realt.onliner.by/2025/12/06/minsk-iz-starogo-alboma',
    'https://tech.onliner.by/2025/12/06/astrapoglyad-golosovanie',
    'https://www.nbrb.by/apihelp/exrates',
    'https://auto.onliner.by/2025/12/06/autoshow-la',
    'https://catalog.onliner.by/',
    'https://r.onliner.by/pk/',
    'https://www.onliner.by/',
    'https://realt.onliner.by/2025/12/06/minsk-iz-starogo-alboma',
    'https://tech.onliner.by/2025/12/06/astrapoglyad-golosovanie',
    'https://www.nbrb.by/apihelp/exrates',
    'https://auto.onliner.by/2025/12/06/autoshow-la',
    'https://catalog.onliner.by/',
    'https://r.onliner.by/pk/',
]

threads = []
function_start_time = time.time()

logging.info(f'Вариант 2 -threading: Работа функции download_content.')

for url in urls:
    thread = threading.Thread(target=download_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


function_end_time = time.time()
function_operation_time = function_end_time - function_start_time


hours = int(function_operation_time // 3600)
minutes = int((function_operation_time % 3600) // 60)
seconds = int(function_operation_time % 60)
formatted_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

logging.info(f'Время выполнения: {formatted_time}.')
print(f'Время выполнения: {formatted_time}.')
