# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
x_resolution = 1000
y_resolution = 600
sd.resolution = (x_resolution, y_resolution)

N = 100
snowflakes = []
snowflakes_lenght = []

for _ in range(N):
    x = sd.random_number(-100, x_resolution)
    y = sd.random_number(y_resolution - 50, y_resolution + 1000)
    point = sd.get_point(x, y)
    snowflakes.append(point)
    snowflakes_lenght.append((sd.random_number(10, 40)))

while True:
    i = 0
    sd.start_drawing()
    for point in snowflakes:
        if (snowflakes[i].y > 30):
            sd.snowflake(center=point, length=snowflakes_lenght[i], color=sd.background_color,)
            point.y -= sd.random_number(1,30)
            point.x += sd.random_number(0, 10)
            sd.snowflake(center=point, length=snowflakes_lenght[i], color=sd.COLOR_WHITE)
            snowflakes[i] = point
        else:
            point.x = sd.random_number(0, x_resolution)
            point.y = sd.random_number(y_resolution - 50, y_resolution + 800)
            snowflakes[i] =point
        i += 1
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()



# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
