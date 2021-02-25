# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def analyse_line(line):
    words_line = line.split(' ')
    if len(words_line) < 3:
        raise ValueError('НЕ присутсвуют все три поля')

    for letter in words_line[0]:
        if not letter.isalpha():
            raise NotNameError('поле имени содержит НЕ только буквы:')

    if '@' not in words_line[1] or '.' not in words_line[1]:
        raise NotEmailError('поле емейл НЕ содержит @ и .(точку):')

    try:
        int(words_line[2])
        if int(words_line[2]) > 99 or int(words_line[2]) < 10:
            raise ValueError('поле возраст НЕ является числом от 10 до 99:')
    except ValueError:
        raise ValueError('поле возраст НЕ является числом от 10 до 99:')

    return ' '.join(words_line)


class ParserLog:

    def __init__(self, filename):
        self.filename = filename

    def analyse_log(self):
        file_log = open(self.filename, mode='r', encoding='utf8')
        file_good_result = open('registrations_good_log.txt', mode='w', encoding='utf8')
        file_bad_result = open('registrations_bad_log.txt', mode='w', encoding='utf8')
        for line in file_log:
            line = line.rstrip()
            try:
                file_good_result.write(analyse_line(line) + '\n')
            except (ValueError, NotNameError, NotEmailError) as exc:
                file_bad_result.write(line + ' - ' + str(exc)+'\n')
        file_log.close()
        file_good_result.close()
        file_bad_result.close()

    def write_result_time_period(self):
        pass


log_stat = ParserLog(filename='registrations.txt')
log_stat.analyse_log()
