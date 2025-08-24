import argparse
import locale
import os
from threading import Thread
import sys

# Функция, которая определяет и возвращает язык системы пользователя. Если языка нет в description то, возвращает en.
def get_language_description():
    lang, _ = locale.getlocale() # Получаем язык системы

    description = {
        'ru': 'Скрипт предназначен для выполнения операций над файлами в каталогах с большой вложенностью. '
              'Доступные операции: поиск, копирование, перемещение файлов. Возможен поиск всех файлов либо '
              'только файлов указанного типа. Текущая версия скрипта: 0.9',
        'en': 'The script is designed to perform operations on files in directories with a large nesting. '
              'Available operations: search, copy, move files. It is possible to search for all files or '
              'only files of a specified type. Current version of the script: 0.9',
    } # Поддерживаемые языки

    return description.get(lang.split('_')[0], description['en']) # Возвращаем язык

# Функция, которая заходит в каталоги и ищет там файлы
def main(input):
    list_of_dirs = [] # Пустой список, в который будем класть директории
    all_files = [] # Здесь будем хранить все файлы в каталоге
    abs_path_list = [] # Здесь будем хранить полные пути к каталогам
    os.chdir(input) # Заходим в рабочий каталог
    print(f"Вход в каталог: {os.getcwd()}")
    list_of_files = os.listdir() # Получаем список всех элементов
    print(f"Список всех элементов в каталоге: {list_of_files}")
    for file in list_of_files: # Проходим по всем элементам и определяем файлы
        if os.path.isfile(file):
            all_files.append(file)
    for dir in list_of_files: # Проходим по всем элементам и определяем каталоги
        if os.path.isdir(dir):
            list_of_dirs.append(dir) # Помещаем каталоги в список
    print(f"Список всех файлов в этом каталоге: {all_files}")
    print(f"Список всех каталогов в этом каталоге: {list_of_dirs}")
    for i in list_of_dirs: # Проходим по всем каталогам в списке
        abs_path = os.path.abspath(i)  # Для каждого определяем абсолютный путь
        print(f"Абсолютный путь к вложенному каталогу: {abs_path}")
        abs_path_list.append(abs_path)  # Помещаем эти абсолютные пути в список
    print(f"Список всех абсолютных путей к вложенным каталогам: {abs_path_list}")
    for j in abs_path_list: # Проходим по всем абсолютным путям в списке и для каждого вызываем main() (рекурсия)
        main(j)

parser = argparse.ArgumentParser(description=get_language_description()) # Вся морока с argparse нужна чтобы всё необходимое передавать в виде аргументов командной строки (терминала).
parser.add_argument("--input", type=str, required=True, help="The directory in which the script searches for files.")
parser.add_argument("--what", type=str, default='search', choices=['search, copy, move'], help="Available actions. For copy and move required output directory.")
parser.add_argument("--output", type=str, help="Directory to which files will be copied/moved")
parser.add_argument("--type", type=str, help="What types of files will be found. Default - all files.")
parser.add_argument("--threads", type=bool, default=False, help="Whether nested directories will be processed multithreaded.")
parser.add_argument("--verbose", type=bool, default=False, help="Outputs full information.")
parser.add_argument("--limit", type=int, default=1000, help="Limit the number of recursive calls.")
args = parser.parse_args()
main(args.input)