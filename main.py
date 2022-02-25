from pywebio.input import input, FLOAT
from pywebio.output import put_text
import argparse
import asyncio

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async

def main():
    put_markdown("## Решение задачек по информатики ##")
    task_type = select("Какую задачу хочешь решить", ['Расчитать обьём видеопамяти',
    'Узнать размер файла изображения', 'Узнать максимально возможное число цветов в изображении'])
    if task_type == 'Расчитать обьём видеопамяти':
        data = input_group("Basic info", [
            input('Input monitor_resolution1', name='monitor_resolution1',type=FLOAT),
            input('Input monitor_resolution2', name='monitor_resolution2',type=FLOAT),
            input('Input colors', name='colors',type=FLOAT)
        ])
        monitor_resolution1 = data['monitor_resolution1']
        monitor_resolution2 = data['monitor_resolution2']
        monitor_result = monitor_resolution2 * monitor_resolution1
        colors = data['colors']
        two_in_power = 2
        power = 1
        while two_in_power <= colors:
            two_in_power *= 2
            power += 1
            bit = power - 1

        result = monitor_result * bit / 8 / 1024
        #print(f"Ответ {result} Кбайт")
        put_text(f"Ответ {result} Кбайт")
    elif task_type == 2:
        monitor_resolution1 = int(input("Разрешение экрана 1 число "))
        monitor_resolution2 = int(input("Разрешение экрана 2 число "))
        monitor_result = monitor_resolution2 * monitor_resolution1
        bit = int(input("Сколько байт для одного пикселя "))

        result = monitor_result * bit / 2 ** 20
        #print(f"Ответ {result} Мбайт")
        put_markdown(f"Ответ {result} Мбайт")

    elif task_type == 3:
        monitor_resolution1 = int(input("Разрешение изображения 1 число "))
        monitor_resolution2 = int(input("Разрешение изображения 2 число "))
        monitor_result = monitor_resolution2 * monitor_resolution1
        colors = int(input("Сколько Кбайт для одного пикселя "))
        result = colors * 1024 * 8 / monitor_result
        n = 2 ** result
        #print(int(n) + "цветов")
        put_markdown(int(n) + "цветов")
    else:
        put_markdown("Не знаю такую:(")

if __name__ == '__main__':
    start_server(main, debug=False, port=8080)
