# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.mud = 0
        self.food_cat = 30

    def __str__(self):
        return 'В доме еды осталось {}, еды для кота {}, денег осталось {}, грязь {}'.format(
            self.food, self.food_cat, self.money, self.mud)

    def day_pass(self):
        self.mud += 5


class Man:
    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.isalive = True

    def __str__(self):
        if self.isalive:
            return '{} - сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)
        else:
            return '{} - мерт(ва)'.format(self.name)

    def eat(self):
        if self.house.food > 0:
            if self.house.food < 10:
                food_portion = self.house.food
            elif self.house.food < 20:
                food_portion = randint(10, self.house.food)
            else:
                food_portion = 20
            self.fullness += food_portion
            self.house.food -= food_portion
            cprint('{} покушал(а), порция составила {} грамм!'.format(self.name, food_portion), color='green')
        else:
            cprint('В доме нет еды!', color='red')
            if self.fullness < 10:
                self.fullness -= self.fullness
            else:
                self.fullness -= 10

    def pet_cat(self):
        self.fullness -= 10
        self.happiness += 15
        cprint('{} погладил(а) кота!'.format(self.name), color='green')


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return 'Муж ' + super().__str__()

    def act(self):
        if self.isalive:
            if self.house.mud >= 90:
                self.happiness -= 10

            if self.fullness < 11:
                self.eat()
            elif self.house.money < 100:
                self.work()
            elif self.house.food_cat < 15:
                self.buy_food_cat()
            else:
                dice = randint(1, 5)
                if dice == 1:
                    self.pet_cat()
                elif dice == 2:
                    self.gaming()
                elif dice == 3:
                    self.buy_food_cat()
                elif dice == 4:
                    self.work()
                else:
                    self.pet_cat()

            if self.happiness <= 0:
                cprint('{} умер от депрессии...'.format(self.name), color='red')
                self.isalive = False
            elif self.fullness <= 0:
                cprint('{} умер от голода...'.format(self.name), color='red')
                self.isalive = False

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        cprint('{} поработал и заработал 150 рублей'.format(self.name), color='green')

    def gaming(self):
        cprint('{} поиграл в танки'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 10

    def buy_food_cat(self):
        self.fullness -= 10
        if self.house.money >= 20:
            self.house.food_cat += 20
            self.house.money -= 20
            cprint('{} купил 20 грамм еды для кота'.format(self.name), color='green')
        elif self.house.money >= 10:
            self.house.food_cat += 10
            self.house.money -= 10
            cprint('{} купил 10 грамм еды для кота'.format(self.name), color='green')
        else:
            cprint('Нет денег на еду для кота', color='red')


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return 'Жена ' + super().__str__()

    def act(self):
        if self.isalive:
            if self.house.mud >= 90:
                self.happiness -= 10

            if self.fullness < 11:
                self.eat()
            elif self.house.food <= 30:
                self.shopping()
            elif self.happiness <= 40:
                if self.house.money > 350:
                    self.buy_fur_coat()
                else:
                    self.pet_cat()
            elif self.house.mud >= 90:
                self.clean_house()
            else:
                dice = randint(1, 5)
                if dice == 1:
                    self.clean_house()
                elif dice == 2:
                    # self.eat()
                    self.clean_house()

                elif dice == 3 and self.house.money > 350:
                    self.buy_fur_coat()
                elif dice == 4:
                    self.pet_cat()
                else:
                    self.shopping()

            if self.happiness <= 0:
                cprint('{} умерла от депрессии...'.format(self.name), color='red')
                self.isalive = False
            if self.fullness <= 0:
                cprint('{} умерла от голода...'.format(self.name), color='red')
                self.isalive = False

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 50:
            self.house.food += 50
            self.house.money -= 50
            cprint('{} купила 50 грамм еды'.format(self.name), color='green')
        elif self.house.money >= 20:
            self.house.food += 20
            self.house.money -= 20
            cprint('{} купила 10 грамм еды'.format(self.name), color='green')
        else:
            cprint('Нет денег на еду', color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            cprint('{} купила шубу и потратила 350 рублей'.format(self.name), color='green')
        else:
            cprint('Нет денег на шабу', color='red')

    def clean_house(self):
        if self.house.mud > 100:
            clean_level = randint(40, 100)
        else:
            clean_level = randint(0, self.house.mud)
        self.fullness -= 10
        self.house.mud -= clean_level
        cprint('{} убрала {} грязи'.format(self.name, clean_level), color='green')


class Cat:

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 30
        self.house = house
        self.isalive = True

    def __str__(self):
        if self.isalive:
            return 'Кот {} - сытость {}'.format(self.name, self.fullness)
        else:
            return 'Котик {} - мерт'.format(self.name)

    def act(self):
        if self.isalive:

            if self.fullness < 11:
                self.eat()

            else:
                dice = randint(1, 3)
                if dice == 1:
                    self.eat()
                elif dice == 2:
                    self.sleep()
                else:
                    self.soil()

            if self.fullness <= 0:
                cprint('{} умер от голода...'.format(self.name), color='red')
                self.isalive = False

    def eat(self):
        if self.house.food_cat > 0:
            if self.house.food_cat < 10:
                food_portion = randint(0, self.house.food_cat)
            else:
                food_portion = randint(0, 10)
            self.fullness += food_portion * 2
            self.house.food_cat -= food_portion
            cprint('Кот {} покушал, порция составила {} грамм!'.format(self.name, food_portion), color='green')
        else:
            cprint('В доме нет еды!', color='red')
            if self.fullness < 10:
                self.fullness -= self.fullness
            else:
                self.fullness -= 10

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} спал целый день!'.format(self.name), color='green')

    def soil(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('Кот {} драл обои спал целый день!'.format(self.name), color='green')


class Child(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.happiness = 100

    def __str__(self):
        return 'Ребенок ' + super().__str__()

    def act(self):
        if self.isalive:
            if self.fullness <= 20:
                self.eat()
            else:
                self.sleep()

            if self.fullness <= 0:
                cprint('{} умер от голода...'.format(self.name), color='red')
                self.isalive = False

    def eat(self):
        if self.house.food > 0:
            if self.house.food < 10:
                food_portion = self.house.food
            else:
                food_portion = 10
            self.fullness += food_portion
            self.house.food -= food_portion
            cprint('{} покушал(а), порция составила {} грамм!'.format(self.name, food_portion), color='green')
        else:
            cprint('В доме нет еды!', color='red')
            if self.fullness < 10:
                self.fullness -= self.fullness
            else:
                self.fullness -= 10

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='green')
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
masik = Cat(name='Масик', house=home)

alesha = Child(name='Алеша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    alesha.act()
    serge.act()
    masha.act()
    masik.act()

    home.day_pass()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(alesha, color='cyan')
    cprint(masik, color='cyan')
    cprint(home, color='cyan')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
