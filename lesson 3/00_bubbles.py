# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(1):
        color_R=random.randint(0,255)
        color_G=random.randint(0,255)
        color_B=random.randint(0,255)

        sd.circle(center_position=point, radius=radius, width=1, color=(color_R,color_G,color_B))
        radius += step

# Нарисовать 10 пузырьков в ряд


# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
        point = sd.random_point()
        step = random.randint(2, 10)
        bubble(point=point, step=step)

sd.pause()
