# -*- coding: utf-8 -*-

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def draw_rainbow(point, radius):
    point_center_rainbow = point
    radius_rainbow = radius
    for current_colors in rainbow_colors:
        sd.circle(center_position=point_center_rainbow, radius=radius_rainbow,color=current_colors, width=8)
        radius_rainbow=radius_rainbow-8

def draw_sun(point_center_sun, radius_rainbow):
    sd.circle(center_position=point_center_sun,radius=radius_rainbow,color=sd.COLOR_YELLOW, width=radius_rainbow)
    for i in range(12):
        ray = sd.get_vector(start_point=point_center_sun, angle=i*30,length=100)
        sd.line(ray.start_point, ray.end_point, width=3)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво