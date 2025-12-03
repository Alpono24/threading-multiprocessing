
import threading   # Импортируем модуль threading для работы с потоками

import requests  # Импортируем библиотеку requests для отправки HTTP-запросов

def download_content(url):
    response = requests.get(url) # Отправляем GET-запрос на указанный URL
    print(f"Содержимое {url} имеет размер {len(response.text)} символов") # Выводим размер полученного содержимого
    for thr in threading.enumerate(): # Перебираем все активные потоки
        print(f'Поток: {thr}')  # Выводим информацию о каждом потоке

urls = [
    'https://www.youtube.com/',
    'https://www.onliner.by/',
    'https://www.nbrb.by/apihelp/exrates',
    'https://alpono24.pythonanywhere.com/',
    'https://lms.teachmeskills.com/attachments/student/11180',
]

threads = [] # Список для хранения созданных потоков

for url in urls:
    thread = threading.Thread(target=download_content, args=(url,))  # Создаем поток для функции download_content с аргументом url
    threads.append(thread) # Добавляем поток в список
    thread.start() # Запуск потока

for thread in threads:
    thread.join()  # Ожидаем завершения каждого потока

print("Все страницы загружены")
