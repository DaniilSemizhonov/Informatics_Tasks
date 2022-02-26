import tornado.ioloop
import tornado.web
from pywebio.input import *
from pywebio.output import *
import tornado.web
from pywebio.platform.tornado import webio_handler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
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
        put_text(f"Ответ {result} Кбайт")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/tool", webio_handler(main())),  # `task_func` is PyWebIO task function
    ])
    application.listen(port=80, address='localhost')
    tornado.ioloop.IOLoop.current().start()