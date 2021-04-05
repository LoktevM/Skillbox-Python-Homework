# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import os


class SecidAnalyzer:

    def __init__(self, file_name, file_dir):
        self.secid_name = None
        self.file_name = file_name
        self.file_dir = file_dir
        self.volatility = 0

    def run(self):
        file_Secid = open(os.path.join(self.file_dir, self.file_name), mode='r', encoding='utf8')
        count_line = 0

        for line in file_Secid:
            words_line = line.split(',')
            if count_line == 1:
                self.file_name = words_line[0]
                curr_price = float(words_line[2])
                min_price = curr_price
                max_price = curr_price
            if count_line > 1:
                curr_price = float(words_line[2])
                if curr_price < min_price:
                    min_price = curr_price
                if curr_price > max_price:
                    max_price = curr_price
            count_line += 1
        average_price = (min_price + max_price) / 2
        #   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
        self.volatility = ((max_price - min_price) / average_price) * 100
        return self.volatility

path_scan_folder = 'E:\Phyton my tests\Skillbox\Lessons\lesson_012\\trades'
fileList = os.listdir(path_scan_folder)
all_volatility = {}
zero_volatility = []
value_volatility = []
for filename in fileList:
    testSecid = SecidAnalyzer(file_name=filename, file_dir=path_scan_folder)
    all_volatility.setdefault(filename, testSecid.run())
all_volatility = sorted(all_volatility.items(), key=lambda x: x[1])

for key, items in all_volatility:
    curr_ticker = (key, items)
    if items == 0:
        zero_volatility.append(curr_ticker)
    else:
        value_volatility.append(curr_ticker)

print("Максимальная волатильность:")
print(value_volatility[-1][0] + ' - ' + str(round(value_volatility[-1][1],2)) + ' %')
print(value_volatility[-2][0] + ' - ' + str(round(value_volatility[-2][1],2)) + ' %')
print(value_volatility[-3][0] + ' - ' + str(round(value_volatility[-3][1],2)) + ' %')

print("Минимальная волатильность:")
print(value_volatility[2][0] + ' - ' + str(round(value_volatility[2][1],2)) + ' %')
print(value_volatility[1][0] + ' - ' + str(round(value_volatility[1][1],2)) + ' %')
print(value_volatility[0][0] + ' - ' + str(round(value_volatility[0][1],2)) + ' %')

print("Нулевая волатильность:")
for ticker in zero_volatility:
    print(ticker[0], end=', ')