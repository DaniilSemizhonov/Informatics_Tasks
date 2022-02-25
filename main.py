from pywebio import start_server
from pywebio.input import *
from pywebio.output import *


def main():
    put_markdown("## Решение задачек по информатики ##")
    put_markdown(" <a href =\"https://github.com/DaniilSemizhonov/Informatics_Tasks\">Исходный код проекта</a>")
    task_type = select("Какую задачу хочешь решить", ['Расчитать обьём видеопамяти',
    'Узнать размер файла изображения', 'Узнать максимально возможное число цветов в изображении'])
    if task_type == 'Расчитать обьём видеопамяти':
        data = input_group("Условия задачи", [
            input('Разрешение монитора первое число', name='monitor_resolution1',type=FLOAT),
            input('Разрешение монитора второе число', name='monitor_resolution2',type=FLOAT),
            input('Количество цветов', name='colors',type=FLOAT)
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
    elif task_type == "Узнать размер файла изображения":
        data = input_group("Условия задачи", [
            input('Разрешение монитора первое число', name='monitor_resolution1', type=FLOAT),
            input('Разрешение монитора второе число', name='monitor_resolution2', type=FLOAT),
            input('Сколько байт для одного пикселя', name='bit', type=FLOAT)
        ])
        monitor_resolution1 = data['monitor_resolution1']
        monitor_resolution2 = data['monitor_resolution2']
        monitor_result = monitor_resolution2 * monitor_resolution1
        bit = data['bit']

        result = monitor_result * bit / 2 ** 20
        #print(f"Ответ {result} Мбайт")
        put_markdown(f"Ответ {result} Мбайт")

    elif task_type == "Узнать максимально возможное число цветов в изображении":
        data = input_group("Условия задачи", [
            input('Разрешение монитора первое число', name='monitor_resolution1', type=FLOAT),
            input('Разрешение монитора второе число', name='monitor_resolution2', type=FLOAT),
            input('Сколько Кбайт для одного пикселя', name='bit', type=FLOAT)
        ])
        monitor_resolution1 = data['monitor_resolution1']
        monitor_resolution2 = data['monitor_resolution2']
        monitor_result = monitor_resolution2 * monitor_resolution1
        colors = data['bit']
        result = colors * 1024 * 8 / monitor_result
        n = 2 ** result
        #print(int(n) + "цветов")
        put_markdown(int(n) + "цветов")

if __name__ == '__main__':
    start_server(main, debug=False, port=8080)
