# Multiprocessing
# Каналы предоставляют двустороннюю связь между двумя процессами.
# Канал создается с помощью Pipe(), возвращающей два объекта соединения, которые могут
# использоваться для отправки и получения данных.

import multiprocessing  # Библиотека для управления параллельными процессами
import time             # Для функции sleep(), используемой для моделирования задержек

# Функция отправки сообщений
def sender(conn):
    for i in range(5):                       # Повторяем пять раз
        time.sleep(1)                         # Задерживаем отправку на 1 сек (эмулируем паузу)
        message = f'Message {i}'              # Формируем сообщение вида "Message X"
        conn.send(message)                    # Посылаем сообщение по соединению Pipe
        print(f'Sender: The {message} has been sent')  # Печать статуса отправки
    conn.send(None)                           # Специальный маркер конца передачи
    conn.close()                              # Закрываем соединение после завершения отправки

# Функция приема сообщений
def receiver(conn):
    while True:                             #  Цикл для постоянного чтения сообщений
        message = conn.recv()               # Чтение сообщения из соединения Pipe
        if message is None:                 # Проверяем, получили ли конец передачи
            break                           # Если да, прекращаем чтение
        print(f'Receiver: {message} received')  # Печать принятого сообщения
        time.sleep(2)                        # Эмуляция длительной обработки сообщения

# Основная точка запуска программы
if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()  # Создание двунаправленного канала связи
    sender_process = multiprocessing.Process(target=sender, args=(child_conn,))  # Процесс-отправитель
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))  # Процесс-получатель

    sender_process.start()      # Запускаем процесс отправителя
    receiver_process.start()    # Запускаем процесс получателя

    sender_process.join()       # Дожидаемся завершения процесса отправителя
    receiver_process.join()     # Дожидаемся завершения процесса получателя

    print('The processes are completed')  # Окончательное подтверждение завершения обоих процессов

