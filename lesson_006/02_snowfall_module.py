# -*- coding: utf-8 -*-
import simple_draw as sd

from snowfall import create_snowflakes, draw_snowflakes, move_snowflakes, get_numbers_fallen_snowflakes, \
    delete_snowflakes

count_sl = 40
create_snowflakes(count_snowflakes=count_sl)

while True:
    draw_snowflakes(color=sd.background_color)
    move_snowflakes()
    draw_snowflakes(color=sd.COLOR_WHITE)

    numbers_snowflakes=get_numbers_fallen_snowflakes()

    count_news=len(numbers_snowflakes)

    if len(numbers_snowflakes)>0:
        print(numbers_snowflakes)
        delete_snowflakes(numbers_snowflakes)
        create_snowflakes(count_snowflakes=count_news)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#     #  нарисовать_снежинки_цветом(color=sd.background_color)
#     #  сдвинуть_снежинки()
#     #  нарисовать_снежинки_цветом(color)
#     #  если есть номера_достигших_низа_экрана() то
#     #       удалить_снежинки(номера)
#     #       создать_снежинки(count)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
