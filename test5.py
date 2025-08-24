import argparse
import locale
import os
from threading import Thread
from pathlib import Path

def main(input):
    list_of_dirs = [] # Пустой список, в который будем класть директории
    abs_path_list = [] # Здесь будем хранить полные пути к каталогам
    os.chdir(input) # Заходим в рабочий каталог
    print(f"Вход в каталог: {os.getcwd()}")
    list_of_files = os.listdir() # Получаем список всех элементов
    print(f"Список всех элементов в каталоге: {list_of_files}")
    for file in list_of_files: # Проходим по всем элементам и определяем файлы
        if os.path.isfile(file):
            print(f"Файлы в текущем каталоге: {file}")
    for dir in list_of_files: # Проходим по всем элементам и определяем каталоги
        if os.path.isdir(dir):
            list_of_dirs.append(dir) # Помещаем каталоги в список
    print(f"Список всех каталогов в этом каталоге: {list_of_dirs}")
    for i in list_of_dirs: # Проходим по всем каталогам в списке
        abs_path = os.path.abspath(i) # Для каждого определяем абсолютный путь
        print(f"Абсолютный путь к вложенному каталогу: {abs_path}")
        abs_path_list.append(abs_path) # Помещаем эти абсолютные пути в список
    print(f"Список всех абсолютных путей к вложенным каталогам: {abs_path_list}")
    for j in abs_path_list: # Проходим по всем абсолютным путям в списке и для каждого вызываем main() (рекурсия)
        main(j)

parser = argparse.ArgumentParser(description='') # Вся морока с argparse нужна чтобы всё необходимое передавать в виде аргументов командной строки (терминала).
parser.add_argument("--input", type=str, required=True, help="The directory in which the script searches for files.")
args = parser.parse_args()
main(args.input)