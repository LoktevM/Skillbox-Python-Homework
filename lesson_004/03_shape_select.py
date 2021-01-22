# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


print('Возможные фигуры:')
print('3 - треугольник')
print('4 - квадрат')
print('5 - пятиугольник')
print('6 - шестиугольник')
print('n - n-угольник')

while 1==True:
    shape_number = input('Введите желаемый номер: ')
    if int(shape_number)>2:
        draw_shape(point=sd.get_point(300, 300), angle=0, color=sd.COLOR_PURPLE,  count_sides=int(shape_number), length=100)
        print('Фигура успешно построена')
        break
    else:
        print('Некорректный номер')
sd.pause()
