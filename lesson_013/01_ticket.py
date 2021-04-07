# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# class TickerMaker():
#     def __init__(self):
#
#
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date):
    template_path = "E:\Phyton my tests\Skillbox\Lessons\lesson_013\images\\ticket_template.png"
    im = Image.open(template_path)
    draw = ImageDraw.Draw(im)
    font_path = 'E:\Phyton my tests\Skillbox\Lessons\lesson_013\images\\fonts\ofont.ru_Vezitsa.ttf'
    font = ImageFont.truetype(font_path, 20)

    draw.text((47, 125), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((47, 190), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((47, 260), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((250, 260), date, font=font, fill=ImageColor.colormap['black'])
    im.show()

make_ticket(fio='Локтева В.М', from_='Москва', to='Лондон', date='29.07.2036')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
