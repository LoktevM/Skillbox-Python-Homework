# -*- coding: utf-8 -*-
from termcolor import cprint
from random import randint


# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды для кота'.format(self.name), color='red')
            if self.fullness <= 0:
                cprint('{} кот умер'.format(self.name), color='red')
            else:
                self.fullness -= 10


    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def destroy(self):
        cprint('{} драл обои целый день'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.destroy()

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            if self.fullness <= 0:
                cprint('{} чувак умер'.format(self.name), color='red')


    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')
    def pick_up_cat(self, cat):
        if self.house:
            cat.house = self.house
            self.fullness -= 10
            cprint('{} подобрал кота {}'.format(self.name, cat.name), color='cyan')
        else:
            cprint('Найди себе дом нищеброд', color='red')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} Сделал уборку дома'.format(self.name), color='green')
        self.fullness -= 20
        self.house.mud -= 100

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 25:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food<20:
            self.buy_cat_food()
        elif self.house.money < 50:
            self.work()
        elif self.house.mud>=100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота осталось {}, грязь {}'.format(
            self.food, self.money, self.cat_food,self.mud)


chuvak = Man(name='Чувак')
my_sweet_home = House()

my_cat = Cat(name='Масик')
second_cat = Cat(name='Пушок')

chuvak.go_to_the_house(house=my_sweet_home)
chuvak.pick_up_cat(cat=my_cat)
chuvak.pick_up_cat(cat=second_cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    chuvak.act()
    my_cat.act()
    second_cat.act()
    print('--- в конце дня ---')
    print(chuvak)
    print(my_cat)
    print(second_cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
