
# Для создания потока в Python с использованием класса можно наследоваться от класса Thread и переопределить
# метод run, который будет выполняться в потоке.

import threading  # Импортируем модуль threading для работы с потоками
import time  # Импортируем модуль time для использования функции sleep

class PrintNumbersThread(threading.Thread):  # Создаем класс PrintNumbersThread, наследующийся от threading.Thread
    def __init__(self, name):  # Конструктор класса с параметром name
        threading.Thread.__init__(self)  # Вызываем конструктор родительского класса threading.Thread
        self.name = name  # Сохраняем имя потока

    def run(self):  # Метод run, который будет выполняться в отдельном потоке
        print(f'Поток {self.name} начал выполнение')  # Выводим сообщение о начале выполнения потока
        for i in range(5):  # Цикл, который выполняется 5 раз
            time.sleep(1)  # Приостанавливаем выполнение потока на 1 секунду
            print(f'{self.name} - число {i}')  # Выводим текущее число с указанием имени потока
        print(f'Поток {self.name} завершил выполнение')  # Выводим сообщение о завершении потока

thread1 = PrintNumbersThread(name='Thread-1')  # Создаем первый поток с именем 'Thread-1'
thread2 = PrintNumbersThread(name='Thread-2')  # Создаем второй поток с именем 'Thread-2'
thread3 = PrintNumbersThread(name='Thread-3')  # Создаем второй поток с именем 'Thread-3'
thread4 = PrintNumbersThread(name='Thread-4')  # Создаем второй поток с именем 'Thread-4'

thread1.start()  # Запускаем первый поток
thread2.start()  # Запускаем второй поток
thread3.start()  # Запускаем третий поток
thread4.start()  # Запускаем четвертый поток

count = 0
for thr in threading.enumerate():  # Перебираем все активные потоки
    print(f'Поток №{count+1}: {thr}')  # Выводим информацию о каждом потоке
    count +=1

thread1.join()  # Ожидаем завершения первого потока
thread2.join()  # Ожидаем завершения второго потока
thread3.join()  # Ожидаем завершения третьего потока
thread4.join()  # Ожидаем завершения четвертого потока

print(f'Количество потоков {count}. Потоки завершены!')  # Выводим сообщение после завершения обоих потоков