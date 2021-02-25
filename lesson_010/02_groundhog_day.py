# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777
current_carma_level = 0


class IamGodError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

class SuicideError(Exception):
    pass


def one_day():
    dice_exception = randint(1, 13)
    if dice_exception == 13:
        dice_exception = randint(1, 6)
        if dice_exception == 1:
            raise IamGodError('Я возомнил себя Богом')
        if dice_exception == 2:
            raise DrunkError('Я напился')
        if dice_exception == 3:
            raise CarCrashError('Я попал в аварию')
        if dice_exception == 4:
            raise DepressionError('У меня депрессия')
        if dice_exception == 5:
            raise GluttonyError('Я объелся')
        if dice_exception == 6:
            raise SuicideError('Я покончил с собой')
    else:
        return randint(1, 7)

day_count=1

file_name = 'log_error.txt'
file = open(file_name, mode='w',encoding='utf8')  # mode (режим): запись символьная, кодировка по умолчанию utf8

while current_carma_level<=ENLIGHTENMENT_CARMA_LEVEL:
    try:
        current_carma_level+=one_day()
        print(f'День {day_count} - Текущая карма {current_carma_level}')
    except(IamGodError, DrunkError,CarCrashError,DepressionError,GluttonyError,SuicideError) as exc:
        print(f'День {day_count} - {exc}')
        file.write(f'День {day_count} - {exc}\n')
    finally:
        day_count+=1

file.close()
# https://goo.gl/JnsDqu
