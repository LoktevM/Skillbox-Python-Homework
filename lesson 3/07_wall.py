# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

x_resolution = 620
y_resolution = 600
sd.resolution = (x_resolution, y_resolution)

hight_brick = 50
wight_brick = 100
count_bricks_in_wight = x_resolution // wight_brick + 1
count_bricks_in_hight = y_resolution // hight_brick

def draw_brick(point):
    left_bottom = point
    right_top= sd.get_point(left_bottom.x + wight_brick, left_bottom.y+hight_brick)
    sd.rectangle(left_bottom=left_bottom,right_top=right_top,  width=1)

for j in range(count_bricks_in_hight):
    for i in range(count_bricks_in_wight):
        if j % 2 == 0:
            current_point = sd.get_point(i * wight_brick, j * hight_brick)
        else:
            current_point = sd.get_point(i * wight_brick-wight_brick / 2, j * hight_brick)
        draw_brick(current_point)

sd.pause()
