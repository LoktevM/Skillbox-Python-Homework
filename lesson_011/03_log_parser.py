# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_generator(filename):
    file_log = open(filename, mode='r')
    prev_data_time = file_log.readline()[0:17] + ']'
    non_counter = 0
    for line in file_log:
        data_time = line[0:17] + ']'  # берем из строки даты и время
        if prev_data_time == data_time:
            if line[-4:-1] == 'NOK':
                non_counter += 1
        else:
            yield prev_data_time, non_counter
            prev_data_time = data_time
            non_counter = 0
    file_log.close()


grouped_events = log_generator(filename='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] - {event_count}')
