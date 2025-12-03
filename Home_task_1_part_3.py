# Блок 2. Домашнее задание
# Задание 1. Написать три программы. Каждая из них занимается
# математическими расчетами (возьмите что-то посложнее, не
# просто 2+2, а чтобы это была хорошая такая математическая
# задача, которая требует много времени на свое выполнение).
# • Первая программа должна быть обычным последовательным
# кодом, как мы писали все 35 занятий до этого. Расчёты эта
# программа производит N раз подряд (можно на разных данных
# (лучше на разных данных)).
# • Вторая программа делает всю математику в N потоков. Опять
# же, лучше, чтобы у каждого потока были разные данные. А
# математика одна.
# • Третья программа делает то же самое, но в N процессах. N
# здесь – количество ядер у вас.
# Задание 2. Аналогичная задача: три программы, одна
# последовательная, другая поточная, третья процессная. Но они
# занимаются не математикой, а GET-запросами на любые юрлки.
# Итог. По заданию 1 замерить время выполнения всех трех
# программ, сравнить. По заданию 2 тоже замерить и сравнить.
# Сделать выводы

#Это 3-ая программа из 1-ой задачи (результаты в логе Home_task_information_about_calculations.log)
import multiprocessing   # Импорт модуля multiprocessing для использования возможностей мультипроцессинга
import time
import logging

# Настраиваем логирование
logging.basicConfig(
    filename='Home_task_information_about_calculations.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Объявление функции
def calc_sum_arithmetic_progression(a_one, difference, n):
    """
    Функция расчета суммы n-членов включительно арифметической прогрессии, где:
        a_one - первый член прогрессии
        a_i - i-ый член прогрессии
        difference - разность прогрессии
        n - n-ый член прогрессии
    Расчёт не по формуле для нагрузки!
    """
    result = 0
    for i in range(n):
        a_i = a_one + (i - 1) * difference
        result += a_i + difference
    return result


def worker(args):
    a_one, difference, n = args
    result = calc_sum_arithmetic_progression(a_one, difference, n)
    return result

if __name__ == '__main__':
    # Записываем начало выполнения функции в лог
    logging.info(f'Вариант 3 - multiprocessing: Работа функции calc_sum_arithmetic_progression.')

    with multiprocessing.Pool(processes=16) as pool:
        function_start_time = time.time()  # START работы функции
        inputs = [
                    (1, 11111, 55555555),    # Данные для вычислений
                    (2, 22222, 55555555),    # Данные для вычислений
                    (3, 33333, 55555555),    # Данные для вычислений
                    (4, 44444, 55555555),    # Данные для вычислений
                    (5, 55555, 55555555)     # Данные для вычислений
                  ]

        results = pool.map(worker, inputs)          # Применяем функцию worker ко всем элементам списка inputs

        function_end_time = time.time()  # END работы функции
        function_operation_time = function_end_time - function_start_time  # Расчет времени работы функции

        # Преобразование времени в часы, минуты и секунды
        hours = int(function_operation_time // 3600)
        minutes = int((function_operation_time % 3600) // 60)
        seconds = int(function_operation_time % 60)
        formatted_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'


        logging.info(f'Время выполнения: {formatted_time}.')
        logging.info(f'Результаты: {results}.')

        print(f'Время выполнения: {formatted_time}.')
        print("Результаты:", results)
