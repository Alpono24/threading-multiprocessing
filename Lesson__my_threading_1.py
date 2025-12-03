import threading  # Импортируем модуль threading для работы с потоками

def print_numbers():
    for i in range(5):
        print(i)
    current = threading.current_thread() # current_thread() – Возвращает объект текущего потока
    print(f'1. текущий поток: {current.name}')
    print(f'2. Количество активных потоков: {threading.active_count()}') # active_count() – Возвращает количество активных потоков.
    if thread.is_alive(): # Проверяет, активен ли поток
        print(f'3. {current.name} Поток активен')
    for thr in threading.enumerate():  # Перебираем все активные потоки
        print(f'Поток: {thr}')  # Выводим информацию о каждом потоке

thread = threading.Thread(target=print_numbers) # Создание потока
thread.start() # Запуск потока
thread.join() # Ожидание завершения потока

print('Поток завершен')
