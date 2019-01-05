#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс окружения для ботов.
Начало: 17 апреля 2018 г. 01:23.
Обновлена: 14 сентября 2018 г. 02:59.

"""

# Версия скрипта.  
board_version = '0.1.0'

# Планирование разработки:

# Исправлено в ver.0.1.0:
# -----------------------
# 
# План работ на ver.0.1.X:
# ----------------------
# 1.Создать прототип окружающей среды.

# Подключаем настройки.
import settings

# Подключаем модуль генератора случайных чисел.
import random

class Enviroment:
    """ Пояснение к классу. """
    
    def __init__(self, width = 16, height = 16):
        """ Конструктор класса. Создаёт двухмерный мир. """
        
        # Ширина мира.
        self.board_width = width
        # Высота мира.
        self.board_height = height
        
        # Тестирование.
        # Заполняем цветом весь мир.
        self.board = [settings.EMPTY for loop
                      in range(0, self.board_width * self.board_height)]
        # Заполняем другим цветом границы мира:
        # верхнюю и нижнюю.
        for loop in range(0, self.board_width):
            self.board[loop] = settings.BORDER
            self.board[loop + ((self.board_height - 1) *
                self.board_width)] = settings.BORDER
        # Заполняем другим цветом границы мира:
        # верхнюю и нижнюю.
        for loop in range(0, self.board_height):
            self.board[loop * self.board_width] = settings.BORDER
            self.board[loop * self.board_width +
                self.board_width - 1] = settings.BORDER

    def td_in_l(self, x, y):
        """ Функция перевода декартовых координат в индекс списка.
        (прим. от TwoDimensions_in_List)."""
            
        return (self.board_width * (y - 1) + x - 1)
            
    def random_board(self):
        """ Оставил ради ТЕСТА !!! Временный генератор рендомной картинки. """
        
        self.board = [random.randint(100, 999) for loop
                      in range(0, self.board_width * self.board_height)]                   