# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
from pprint import pprint

def is_happy(number):
    str_number = str(number)
    sum_part_1, sum_part_2 = 0, 0
    for i in range(len(str_number) // 2):
        sum_part_1 += int(str_number[i])
        sum_part_2 += int(str_number[len(str_number) - i - 1])
    if sum_part_1 is not sum_part_2:
        return False
    return True


def is_palyndrom(number):
    str_number = str(number)
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[len(str_number) - i - 1]:
            return False
    return True


class PrimeNumbers:
    def __init__(self, n):
        self.i, self.number, self.n = 0, 2, n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 0
        self.number = 2
        self.prime_numbers = [2]
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            next_number = self.number + 1
            while True:
                for prime in self.prime_numbers:
                    if next_number % prime == 0:
                        break
                else:
                    self.prime_numbers.append(next_number)
                    break
                next_number = next_number + 1
            self.number = next_number
        if self.number > self.n:
            raise StopIteration()
        return self.number


prime_number_iterator = PrimeNumbers(1000)
for number in prime_number_iterator:
    print(number)

result = filter(is_happy, prime_number_iterator)
pprint(list(result))

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик



def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)
# result = filter(is_palyndrom, prime_numbers_generator(n=1000000))
# pprint(list(result))

# result = filter(is_happy, range(50000))
# pprint(list(result))

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
