# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
flakes = []


class Snowflake:
    def __init__(self):
        self.x_coord = sd.random_number(0, sd.resolution[0])
        self.y_coord = sd.random_number(sd.resolution[1] - 50, sd.resolution[1] + 500)

    def move(self):
        self.y_coord -= sd.random_number(10, 20)
        self.x_coord += sd.random_number(-10, 10)

    def draw(self, color):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(self.x_coord, self.y_coord), length=10, color=color)
        sd.finish_drawing()

    def cant_fall(self):
        if self.y_coord < 20:
            return True


def get_flakes(count):
    local_flakes = []
    for _ in range(count):
        local_flakes.append(Snowflake())
    return local_flakes


def get_fallen_snowflakes():
    count_fallen_snowflakes=0
    for point in flakes:
        if point.cant_fall():
            count_fallen_snowflakes+=1
            flakes.remove(point)
    return count_fallen_snowflakes

def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=50)

while True:
    for flake in flakes:
        flake.draw(color=sd.background_color)
        flake.move()
        flake.draw(color=sd.COLOR_WHITE)
    fallen_flakes = get_fallen_snowflakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# flake = Snowflake()
#
# while True:
#     flake.draw(color=sd.background_color)
#     flake.move()
#     flake.draw(color=sd.COLOR_WHITE)
#     if flake.cant_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
