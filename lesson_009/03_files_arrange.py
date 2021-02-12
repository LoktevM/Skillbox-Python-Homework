# -*- coding: utf-8 -*-

import os
import shutil
import time


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


# zip_file_name = 'icons.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for file_name in zfile.namelist():
#     zfile.extract(file_name)

class File_organizer():

    def __init__(self, scan_folder, goal_folder):
        self.scan_folder = scan_folder
        self.goal_folder = goal_folder
        if not os.path.exists(goal_folder):
            os.mkdir(goal_folder)


    def collect_stat(self):
        path_scan_folder = os.path.join(os.path.abspath(os.curdir), self.scan_folder)
        path_goal_folder = os.path.join(os.path.abspath(os.curdir), self.goal_folder)
        print(path_scan_folder)
        for dirpath, dirnames, filenames in os.walk(path_scan_folder):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                path_year = os.path.join(path_goal_folder, str(file_time[0]))
                path_month = os.path.join(path_year, str(file_time[1]))
                path_file = os.path.join(dirpath,file)
                if not os.path.exists(path_year):
                    os.mkdir(path_year)
                if not os.path.exists(path_month):
                    os.mkdir(path_month)
                shutil.copy2(path_file,path_month)

icon_organizer = File_organizer(scan_folder='icons', goal_folder='icons_by_year')
icon_organizer.collect_stat()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
