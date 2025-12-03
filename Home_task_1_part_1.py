# Блок 2. Домашнее задание
# Задание 1. Написать три программы. Каждая из них занимается
# математическими расчетами (возьмите что-то посложнее, не
# просто 2+2, а чтобы это была хорошая такая математическая
# задача, которая требует много времени на свое выполнение).
# • Первая программа должна быть обычным последовательным
# кодом, как мы писали все 35 занятий до этого. Расчёты эта
# программа производит N раз подряд (можно на разных данных
# (лучше на разных данных)).
# • Вторая программа делает всю математику в N потоков. Опять же, лучше, чтобы у каждого потока были разные данные.
# А математика одна.
# • Третья программа делает то же самое, но в N процессах. N
# здесь – количество ядер у вас.
# Задание 2. Аналогичная задача: три программы, одна
# последовательная, другая поточная, третья процессная. Но они
# занимаются не математикой, а GET-запросами на любые юрлки.
# Итог. По заданию 1 замерить время выполнения всех трех
# программ, сравнить. По заданию 2 тоже замерить и сравнить.
# Сделать выводы

#Это 1-ая программа из 1-ой задачи (результаты в логе Home_task_information_about_calculations.log)
import time
import logging

logging.basicConfig(
    filename='Home_task_information_about_calculations.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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

logging.info(f'Вариант 1 - последовательное выполнение/последовательный код: Работа функции calc_sum_arithmetic_progression.')

function_start_time = time.time() # START работы функции
sum_result_1 = calc_sum_arithmetic_progression(1, 11111, 55555555)  # Выполнение функции
sum_result_2 = calc_sum_arithmetic_progression(2, 22222, 55555555)  # Выполнение функции
sum_result_3 = calc_sum_arithmetic_progression(3, 33333, 55555555)  # Выполнение функции
sum_result_4 = calc_sum_arithmetic_progression(4, 44444, 55555555)  # Выполнение функции
sum_result_5 = calc_sum_arithmetic_progression(5, 55555, 55555555)  # Выполнение функции
function_end_time = time.time() # END работы функции
function_operation_time = function_end_time - function_start_time # Расчет времени работы функции

# Преобразование времени в часы, минуты и секунды
hours = int(function_operation_time // 3600)
minutes = int((function_operation_time % 3600) // 60)
seconds = int(function_operation_time % 60)
formatted_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

logging.info(f'Результаты выполнения: [{sum_result_1}, {sum_result_2},{sum_result_3},{sum_result_4},{sum_result_5}].')
logging.info(f'Время выполнения: {formatted_time}.')

print(f'Результаты выполнения: [{sum_result_1}, {sum_result_2},{sum_result_3},{sum_result_4},{sum_result_5}].')
print(f'Время выполнения: {formatted_time}.')