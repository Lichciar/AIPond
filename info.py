#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт, позволяющий выводить информацию в консоль или файл.
Начало: 22 июня 2022 г. 01:53.
Обновлена: 28 июня 2024 г. 16:20."""

# Версия скрипта.  
version = '0.1.1'

# Планирование разработки:

# Выполнено в версии 0.1.0 от 09 января 2024 г.:
# -----------------------
# 1. Настроен контроль версии.
# 2. Реализована самая простая схема вывода информации на консоль.
# 3. Вывод на консоль через F-строки.

# Выполнено в версии 0.1.1 от 28 июня 2024 г.:
# ------------------------
# 1. Подключен модуль работы с датой и временем.
# 2. Добавил вывод времени (output_time) и даты (output_data) сообщений
#    консоль, вместо "ДДММГГ - ДД:ММ".

# План работ на ver.0.1.X:
# --------------------------

import settings # Подключаем настройки.
from time import localtime  # Модуль времени.

def output_data(data):
    """ Функция возвращает в читаемом виде дату."""

    # Формирум крисивый формат вывода текущей даты.
    year = str(data.tm_year)[2:]
    mon = str(data.tm_mon)
    if len(mon) < 2: # Для читабельности добавляем 0.
        mon = "0" + mon
    mday = str(data.tm_mday)
    if len(mday) < 2: # Для читабельности добавляем 0.
        mday = "0" + mday
    return (year + mon + mday)

def output_time(time):
    """ Функция возвращает в читаемом виде время."""

    hours = str(time.tm_hour)
    if len(hours) < 2: # Для читабельности добавляем 0.
        hours = "0" + hours
    minutes = str(time.tm_min)
    if len(minutes) < 2: # Для читабельности добавляем 0.
        minutes = "0" + minutes
    seconds = str(time.tm_sec)
    if len(seconds) < 2: # Для читабельности добавляем 0.
        seconds = "0" + seconds
    return (hours + ':' + minutes + ':' + seconds)

def output(info_object, message):
    """ Функция вывода информации в консоль или файл. 
        info_object - объект который пытается вывести сообщение,
        message - сообщение для вывода.
        Пример команды:
        info.output('board.Enviroment.__init__', 'Примет мир!')
        Пример вывода:
        22.06.22 - 02:15:17 - board.Enviroment.__init__ - Привет мир!."""

    # Проверяем разрешение на вывод сообщения в консоль.
    if settings.INFO_PERMISSION[info_object] == 'console':
        
        current_time = localtime()  # Получаем текущее время и дату.
        print(f'{output_data(current_time)} - {output_time(current_time)}' +
            f'- {info_object} - {message};')
  
# Тестирование.
if __name__ == '__main__':
    
    # Приветствие.
    print(f'Тестирование скрипта info v.{version}')
    # Пробуем вывести сообщение в консоль.
    output('info.__main__', 'Тестирование функции info.output: ' + __name__)