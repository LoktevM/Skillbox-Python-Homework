# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию alpha.is() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from pprint import pprint


# zip_file_name = 'voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for file_name in zfile.namelist():
#     zfile.extract(file_name)

class Stats_of_text:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        with open(self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def sorting(self):
        if self.stat:
            sorted_values=sorted(self.stat.values(), reverse=True)
            self.sorted_stats = {}
            for i in sorted_values:
                for k in self.stat.keys():
                    if self.stat[k] == i:
                        self.sorted_stats[k] = self.stat[k]
                        break

            self.stat = self.sorted_stats

    def print_stat(self):
        txt = '+'
        print(f'+{txt:-^30}+')
        txt = 'Буква'
        txt2 = 'Частота'
        print(f'|{txt:-^14}|{txt2:-^15}|')
        txt = '+'
        print(f'+{txt:-^30}+')
        for char, count in self.stat.items():
            print(f'|{char:^14}|{count:^15}|')
        print(f'+{txt:-^30}+')

stat_vim = Stats_of_text(file_name='voyna-i-mir.txt')
stat_vim.collect()
stat_vim.sorting()
stat_vim.print_stat()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
