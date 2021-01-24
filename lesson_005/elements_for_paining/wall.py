# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

hight_brick = 20
wight_brick = 40

def draw_brick(point,hight_brick,wight_brick):
    left_bottom = point
    right_top = sd.get_point(left_bottom.x + wight_brick, left_bottom.y + hight_brick)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

def draw_wall(point, hight, wight):
    count_bricks_in_wight = wight // wight_brick
    count_bricks_in_hight = hight // hight_brick
    wight_brick_last = wight % wight_brick
    for j in range(count_bricks_in_hight):
        for i in range(count_bricks_in_wight):
            if j % 2 == 0:
                current_point = sd.get_point(point.x + i * wight_brick, point.y + j * hight_brick)
            elif (i<count_bricks_in_wight-1):
                current_point = sd.get_point(point.x + i * wight_brick + wight_brick / 2, point.y + j * hight_brick)
            draw_brick(point=current_point,hight_brick=hight_brick,wight_brick=wight_brick)
        if wight_brick_last>0 and j % 2 == 0:
            current_point = sd.get_point(point.x + (count_bricks_in_wight) * wight_brick, point.y + j * hight_brick)
            draw_brick(current_point,hight_brick=hight_brick,wight_brick=wight_brick_last)