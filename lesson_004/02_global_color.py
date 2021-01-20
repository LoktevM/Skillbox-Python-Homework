# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_shape(point, angle, count_sides, length, color):
    v_first = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    sd.line(v_first.start_point, v_first.end_point, color=color, width=3)
    v_next = v_first
    for i in range(count_sides - 1):
        if (i != count_sides - 2):
            v_next = sd.get_vector(start_point=v_next.end_point, angle=angle + (360 / count_sides) * (i + 1),
                                   length=length,
                                   width=3)
            sd.line(v_next.start_point, v_next.end_point, color=color, width=3)
        else:
            sd.line(v_next.end_point, v_first.start_point, color=color,width=3)


print('Возможный цвета:')
print('1 - красный')
print('2 - оранжевый')
print('3 - желтый')
print('4 - зеленый')
print('5 - голубой')
print('6 - синий')
print('7 - фиолетовый')
# print('Введите номер цвета:')
color_list = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
while 1==True:
    color_number = input('Введите желаемый номер: ')
    if 0<int(color_number)<8:
        color_current=color_list[int(color_number)-1]
        draw_shape(point=sd.get_point(100, 100), angle=30, color=color_current,  count_sides=3, length=100)
        draw_shape(point=sd.get_point(350, 100), angle=30,  color=color_current, count_sides=4, length=100)
        draw_shape(point=sd.get_point(350, 350), angle=0,  color=color_current, count_sides=6, length=100)
        draw_shape(point=sd.get_point(100, 350), angle=50, color=color_current,  count_sides=11, length=50)
        print('Фигуры успешно построены')
        break
    else:
        print('Некорректный номер')
sd.pause()