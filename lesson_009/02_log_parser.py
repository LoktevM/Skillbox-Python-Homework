# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from pprint import pprint

class ParserLog:

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}

    def analyse_minutes(self):
        file_log = open(self.filename, mode='r')
        file_result = open('log_result.txt', mode='w')
        prev_key=None

        for line in file_log:
            data_time = line[0:17]  +']'        #берем из строки даты и время
            if data_time not in self.stat:  #если втсречаем новую строку - печатаем старую и созданием новую
                if prev_key:
                    file_result.write(str(prev_key)+' '+str(self.stat[prev_key])+'\n')
                self.stat[data_time] = 0  #создаем новую строку
            if line[-4:-1] == 'NOK':
                self.stat[data_time] += 1
            prev_key=data_time

        file_result.write(str(prev_key) + ' ' + str(self.stat[prev_key])) #последняя строка

        pprint(self.stat)
        file_log.close()
        file_result.close()

    def write_result_time_period(self):
        pass


log_stat = ParserLog(filename='events.txt')
log_stat.analyse_minutes()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
