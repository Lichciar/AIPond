#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс ботов.
Начало: 30 марта 2018 г. 02:37.
Обновлена: 19 августа 2019 г. 23:23.

"""

# Версия скрипта.  
version = '0.1.1'

# Планирование разработки:

# Исправлено в ver.0.1.1:
# -----------------------
# 1. Класс Resident разделён на класс Bot и Genotype.
# 2. Добавил тестирование класса.
# 3. Сделал инициализацию бота.

# Запланировано в ver.0.1.2:
# -----------------------

# Подключаем настройки.
import settings

# Подключаем модуль генератора случайных чисел.
import random

# Создаём класс бота.
class Bot:
    """ Класс, описывающий поведение и характеристики бота. """
    
    def __init__(self, x = 1, y = 1, cng = 0, number = 0):
        """ Конструктор класса. Создаём бота в мире."""
        
        # Положение счётчика в программе бота (от ProgramStep).
        self.ps = 0
        # Здоровье бота.
        # (A) Временное решение для тестирования.
        self.health = 10 + random.randint(0, 10)
        # Программа бота, пока что произвольная.
        self.cng = cng
        # Положение по оси Х.
        self.x = x
        # Положение по оси Y.
        self.y = y
        # Направление бота.
        self.direction = random.randint(0, 7)
        # Индидуальный номер бота.
        self.number = number
        
# Тестирование класса.
if __name__ == '__main__':
    
    # Приветствие.
    print('Запущено тестирование класса Bot v.', version, '\n')
    
    # Создаём нового бота.
    print('Создаём нового бота:')
    b = Bot(number = 666)
    print('    ps =', b.ps)
    print('    health =', b.health)
    print('    cng =', b.cng)
    print('    x =', b.x)
    print('    y =', b.y)
    print('    direction =', b.direction)
    print('    number =', b.number)