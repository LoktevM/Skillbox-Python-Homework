# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import os
import threading

from utils import time_track

all_volatility = {}


class SecidAnalyzer(threading.Thread):
    def __init__(self, file_name, *args, **kwargs):
        super(SecidAnalyzer, self).__init__(*args, **kwargs)
        self.secid_name = None
        self.file_name = file_name
        self.file_dir = 'E:\Phyton my tests\Skillbox\Lessons\lesson_012\\trades'
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
        all_volatility.setdefault(self.file_name, self.volatility)


@time_track
def main():
    path_scan_folder = 'E:\Phyton my tests\Skillbox\Lessons\lesson_012\\trades'
    fileList = os.listdir(path_scan_folder)
    zero_volatility = []
    value_volatility = []
    Secids = [SecidAnalyzer(file_name=filename) for filename in fileList]
    # for sedic in Secids:
    #     sedic.run()

    for sedic in Secids:
        sedic.start()
    for sedic in Secids:
        sedic.join()
    new_volatility = sorted(all_volatility.items(), key=lambda x: x[1])

    for key, items in new_volatility:
        curr_ticker = (key, items)
        if items == 0:
            zero_volatility.append(curr_ticker)
        else:
            value_volatility.append(curr_ticker)

    print("Максимальная волатильность:")
    print(value_volatility[-1][0] + ' - ' + str(round(value_volatility[-1][1], 2)) + ' %')
    print(value_volatility[-2][0] + ' - ' + str(round(value_volatility[-2][1], 2)) + ' %')
    print(value_volatility[-3][0] + ' - ' + str(round(value_volatility[-3][1], 2)) + ' %')

    print("Минимальная волатильность:")
    print(value_volatility[2][0] + ' - ' + str(round(value_volatility[2][1], 2)) + ' %')
    print(value_volatility[1][0] + ' - ' + str(round(value_volatility[1][1], 2)) + ' %')
    print(value_volatility[0][0] + ' - ' + str(round(value_volatility[0][1], 2)) + ' %')

    print("Нулевая волатильность:")
    for ticker in zero_volatility:
        print(ticker[0], end=', ')
    print(end='\n')


if __name__ == '__main__':
    main()
