# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

print("В комнате room_1 живут:")
for person in room_1.folks:
    print(person)
print("В комнате room_2 живут:")
for person in room_2.folks:
    print(person)
