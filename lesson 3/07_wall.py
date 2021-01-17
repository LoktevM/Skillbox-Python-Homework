# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

x_resolution = 620
y_resolution = 600
sd.resolution = (x_resolution, y_resolution)

hight_brick = 10
wight_brick = 30
count_bricks_in_wight = x_resolution // wight_brick + 1
count_bricks_in_hight = y_resolution // hight_brick


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


def draw_brick(point):
    point_1 = point
    point_2 = sd.get_point(point_1.x + wight_brick, point_1.y)
    point_3 = sd.get_point(point_2.x, point_2.y + hight_brick)
    point_4 = sd.get_point(point_3.x - wight_brick, point_3.y)
    sd.line(start_point=point_1, end_point=point_2, color=sd.COLOR_ORANGE, width=3)
    sd.line(start_point=point_2, end_point=point_3, color=sd.COLOR_ORANGE, width=3)
    sd.line(start_point=point_3, end_point=point_4, color=sd.COLOR_ORANGE, width=3)
    sd.line(start_point=point_4, end_point=point_1, color=sd.COLOR_ORANGE, width=3)

for j in range(count_bricks_in_hight):
    for i in range(count_bricks_in_wight):
        if j % 2 == 0:
            current_point = sd.get_point(i * wight_brick, j * hight_brick)
        else:
            current_point = sd.get_point(i * wight_brick-wight_brick / 2, j * hight_brick)
        draw_brick(current_point)

sd.pause()
