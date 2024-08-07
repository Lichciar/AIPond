#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс ботов.
Начало: 30 марта 2018 г. 02:37.
Обновлена: 22 июня 2022 г. 03:05.

"""

# Версия скрипта.  
version = '0.1.2'

# Планирование разработки:

# Выполнено в ver.0.1.1 от 19 августа 2019 г.:
# ---------------------------------------------
# 1. Класс Resident разделён на класс Bot и Genotype.
# 2. Добавил тестирование класса.
# 3. Сделал инициализацию бота.

# Выполнено в ver.0.1.2:
# -----------------------
# 1. Небольшая правка комментариев.
# 2. Добавлена система фиксирования информации "info".
# 3. Удалена часть кода тестирования класса в виду п. 2.

# План работ на ver.0.1.X:
# --------------------------

import settings # Подключаем настройки.
import info     # Подключаем систему фиксирования работы скрипта.
import random   # Подключаем модуль генератора случайных чисел.

# Создаём класс бота.
class Bot:
    """ Класс, описывающий поведение и характеристики бота. """
    
    def __init__(self, x = 1, y = 1, cng = 0, number = 0):
        """ Конструктор класса. Создаём бота в мире."""
        
        # Вывод работы инициализации класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'bot.Bot.__init__'
        # Вывод информации.
        message = 'Инициализация нового экземпляра класса Bot:'
        info.output(info_object, message)

        # Положение счётчика в программе бота (от ProgramStep).
        self.ps = 0
        # Здоровье бота.
        # (ВНИМАНИЕ) Временное решение для тестирования.
        self.health = 10 + random.randint(0, 10)
        # Генотип бота, пока что произвольная.
        self.cng = cng
        # Положение по оси Х.
        self.x = x
        # Положение по оси Y.
        self.y = y
        # Направление бота.
        self.direction = random.randint(0, 7)
        # Индидуальный номер бота.
        self.number = number
        
        message = '_Счётчик программы генотипа (ps) = ' + str(self.ps)
        info.output(info_object, message)
        message = '_Здоровье (health) = ' + str(self.health)
        info.output(info_object, message)
        message = '_Генотип бота (cng) = ' + str(self.cng)
        info.output(info_object, message)
        message = '_Положение по оси Х (x) = ' + str(self.x)
        info.output(info_object, message)
        message = '_Положение по оси Y (y) = ' + str(self.y)
        info.output(info_object, message)
        message = '_Направление взгляда (direction) = ' + str(self.direction)
        info.output(info_object, message)
        message = '_Номер бота (number) = ' + str(self.number)
        info.output(info_object, message)
        
# Тестирование класса.
if __name__ == '__main__':
    
    # Приветствие.
    print('Запущено тестирование класса Bot v.', version, '\n')
    
    # Создаём нового бота.
    print('Создаём нового бота:')
    b = Bot(number = 666)