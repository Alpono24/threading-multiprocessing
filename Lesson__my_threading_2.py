# Два потока выполняют разные функции параллельно
import threading  # Импортируем модуль threading для работы с потоками
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)
# print_numbers()

def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(letter)
# print_letters()

thread1 = threading.Thread(target=print_numbers)  # Создание потока
thread2 = threading.Thread(target=print_letters)  # Создание потока

thread1.start() # Запуск потока
thread2.start() # Запуск потока

count = 0
for thr in threading.enumerate():  # Перебираем все активные потоки
    print(f'Поток №{count+1}: {thr}')  # Выводим информацию о каждом потоке
    count +=1

thread1.join() # Ожидание завершения потока
thread2.join() # Ожидание завершения потока

print(f'Количество потоков {count}. Потоки завершены!')