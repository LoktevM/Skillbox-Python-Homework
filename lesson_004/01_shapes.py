# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_shape(point, angle, count_sides, length):
    v_first = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    sd.line(v_first.start_point, v_first.end_point, width=3)
    v_next = v_first
    for i in range(count_sides - 1):
        if (i != count_sides - 2):
            v_next = sd.get_vector(start_point=v_next.end_point, angle=angle + (360 / count_sides) * (i + 1),
                                   length=length,
                                   width=3)
            sd.line(v_next.start_point, v_next.end_point, width=3)
        else:
            sd.line(v_next.end_point, v_first.start_point, width=3)


draw_shape(point=sd.get_point(100, 100), angle=30, count_sides=3, length=100)
draw_shape(point=sd.get_point(350, 100), angle=30, count_sides=4, length=100)
draw_shape(point=sd.get_point(350, 350), angle=0, count_sides=6, length=100)
draw_shape(point=sd.get_point(100, 350), angle=50, count_sides=11, length=50)



sd.pause()
