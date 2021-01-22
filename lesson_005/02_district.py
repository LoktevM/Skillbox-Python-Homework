# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1 as cs_h1_r1
import district.central_street.house1.room2 as cs_h1_r2
import district.central_street.house2.room1 as cs_h2_r1
import district.central_street.house2.room2
from district.soviet_street.house1.room1 import folks as people_of_ss_h1_r1
from district.soviet_street.house1.room2 import folks
from district.soviet_street.house2 import room1

razdelitel = ', '
people = []

for person in cs_h1_r1.folks:
    people.append(person)
for person in cs_h1_r2.folks:
    people.append(person)
for person in cs_h2_r1.folks:
    people.append(person)
for person in district.central_street.house2.room2.folks:
    people.append(person)
for person in people_of_ss_h1_r1:
    people.append(person)
for person in folks:
    people.append(person)
for person in room1.folks:
    people.append(person)

new_str = razdelitel.join(people)
print("На районе живут:", new_str)
