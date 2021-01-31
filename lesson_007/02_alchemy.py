# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __init__(self, gift=None):
        self.name='Вода'
    def __str__(self):
        return self.name
    def __add__(self, second_element):
        if isinstance(second_element, Air):
            return Storm()
        elif isinstance(second_element, Fire):
            return Steam()
        elif isinstance(second_element, Ground):
            return Mud()

class Air:
    def __init__(self, gift=None):
        self.name = 'Воздух'
    def __str__(self):
        return self.name

    def __add__(self, second_element):
        if isinstance(second_element, Water):
            return Storm()
        elif isinstance(second_element, Fire):
            return Lighting()
        elif isinstance(second_element, Ground):
            return Dust()
        elif isinstance(second_element, Lava):
            return Stoun()


class Fire:
    def __init__(self, gift=None):
        self.name = 'Огонь'
    def __str__(self):
        return self.name

    def __add__(self, second_element):
        if isinstance(second_element, Air):
            return Lighting()
        elif isinstance(second_element, Water):
            return Steam()
        elif isinstance(second_element, Ground):
            return Lava()
class Ground:
    def __init__(self, gift=None):
        self.name = 'Земля'
    def __str__(self):
        return self.name
    def __add__(self, second_element):
        if isinstance(second_element, Air):
            return Dust()
        elif isinstance(second_element, Water):
            return Mud()
        elif isinstance(second_element, Fire):
            return Lava()

class Storm:
    def __init__(self, gift=None):
        self.name = 'Шторм'
    def __str__(self):
        return self.name

class Steam:
    def __init__(self, gift=None):
        self.name = 'Пар'

    def __str__(self):
        return self.name

class Mud:
    def __init__(self, gift=None):
        self.name = 'Грязь'

    def __str__(self):
        return self.name

class Lighting:
    def __init__(self, gift=None):
        self.name = 'Молния'

    def __str__(self):
        return self.name

class Dust:
        def __init__(self, gift=None):
            self.name = 'Пыль'

        def __str__(self):
            return self.name

class Lava:
    def __init__(self, gift=None):
        self.name = 'Лава'

    def __str__(self):
        return self.name

    def __add__(self, second_element):
        if isinstance(second_element, Air):
            return Stoun()

class Stoun:
    def __init__(self, gift=None):
        self.name = 'Камень'

    def __str__(self):
        return self.name

print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Air(), '+', Ground(), '=', Air() + Ground())
print(Ground(), '+', Fire(), '=', Ground() + Fire())
print(Air(), '+', Lava(), '=', Air() + Lava())
print(Lava(), '+', Air(), '=', Lava() + Air())
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
