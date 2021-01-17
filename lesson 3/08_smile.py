# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(point):
    simple_draw.circle(center_position=point, radius=50, width=3, color=simple_draw.COLOR_BLACK)
    simple_draw.circle(center_position=simple_draw.get_point(point.x+20,point.y+20), radius=6, width=5, color=simple_draw.COLOR_BLACK)
    simple_draw.circle(center_position=simple_draw.get_point(point.x-20,point.y+20), radius=6, width=5, color=simple_draw.COLOR_BLACK)
    simple_draw.line(start_point=simple_draw.get_point(point.x-20,point.y-20), end_point=simple_draw.get_point(point.x+20,point.y-20))

for _ in range(5):

    point = simple_draw.random_point()
    draw_smile(point)

simple_draw.pause()
