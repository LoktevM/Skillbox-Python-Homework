# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

x_resolution = 1000
y_resolution = 600
sd.resolution = (x_resolution, y_resolution)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# def draw_line(start_point, end_point):

# point_start = sd.get_point(50, 50)
# point_end = sd.get_point(350, 450)
#
# for current_colors in rainbow_colors:
#     sd.line(start_point=point_start, end_point=point_end, color=current_colors, width=4)
#     point_start.x += 5
#     point_end.x += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


point_center_rainbow = sd.get_point(x_resolution / 2, 0)
radius_rainbow = x_resolution/2
for current_colors in rainbow_colors:
    sd.circle(center_position=point_center_rainbow, radius=radius_rainbow,color=current_colors, width=8)
    radius_rainbow=radius_rainbow-8

sd.pause()
