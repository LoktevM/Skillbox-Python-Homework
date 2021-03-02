# -*- coding: utf-8 -*-

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
import simple_draw as sd


def get_polygon(n):
    def draw_shape(point, angle, length):
        v_first = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        sd.line(v_first.start_point, v_first.end_point, width=3)
        v_next = v_first
        for i in range(n - 1):
            if i != n - 2:
                v_next = sd.get_vector(start_point=v_next.end_point, angle=angle + (360 / n) * (i + 1),
                                       length=length,
                                       width=3)
                sd.line(v_next.start_point, v_next.end_point, width=3)
            else:
                sd.line(v_next.end_point, v_first.start_point, width=3)

    return draw_shape


draw_triangle = get_polygon(n=8)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
