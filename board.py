#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс окружения для ботов.
Начало: 17 апреля 2018 г. 01:23.
Обновлена: 04 августа 2019 г. 02:51.

"""

# Версия скрипта.  
version = '0.1.1'

# Планирование разработки:

# Исправлено в ver.0.1.0:
# -----------------------
# 1.Создан прототип окружающей среды.
#
# Исправлено в ver.0.1.1:
# -----------------------
# 1.Добавлена функция get_map.
# 
# План работ на ver.0.1.X:
# ----------------------
# 

# Подключаем настройки.
import settings

# Подключаем модуль генератора случайных чисел.
import random

class Enviroment:
    """ Класс описывающий окружающую среду бота. """
    
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
            self.board[loop] = settings.WALL
            self.board[loop + ((self.board_height - 1) *
                self.board_width)] = settings.WALL
        # Заполняем другим цветом границы мира:
        # верхнюю и нижнюю.
        for loop in range(0, self.board_height):
            self.board[loop * self.board_width] = settings.WALL
            self.board[loop * self.board_width +
                self.board_width - 1] = settings.WALL

    def td_in_l(self, x, y):
        """ Функция перевода декартовых координат в индекс списка.
        (прим. от TwoDimensions_in_List)."""
            
        return (self.board_width * (y - 1) + x - 1)

    def get_overview(self, x, y):
        """ Функция получения карты в одну клетку вокруг бота. """

        # 0-1-2
        # 3---4
        # 5-6-7
        overview = []
        overview.append(self.board[self.td_in_l(x - 1, y - 1)]) #0
        overview.append(self.board[self.td_in_l(x, y - 1)])     #1
        overview.append(self.board[self.td_in_l(x + 1, y - 1)]) #2
        overview.append(self.board[self.td_in_l(x - 1, y)])     #3
        overview.append(self.board[self.td_in_l(x + 1, y)])     #4
        overview.append(self.board[self.td_in_l(x - 1, y + 1)]) #5
        overview.append(self.board[self.td_in_l(x, y + 1)])     #6
        overview.append(self.board[self.td_in_l(x + 1, y + 1)]) #7

        return overview

    def set_overview(self, x, y, cell, value):
        """ Функция изменения окружающей среды в одну клетку вокруг
            бота."""

        # 0-1-2
        # 3---4
        # 5-6-7
        if cell == 0:
            self.board[self.td_in_l(x - 1, y - 1)] = value      #0
        elif cell == 1:
            self.board[self.td_in_l(x, y - 1)] = value          #1
        elif cell == 2:
            self.board[self.td_in_l(x + 1, y - 1)] = value      #2
        elif cell == 3:
            self.board[self.td_in_l(x - 1, y)] = value          #3
        elif cell == 4:
            self.board[self.td_in_l(x + 1, y)] = value          #4
        elif cell == 5:
            self.board[self.td_in_l(x - 1, y + 1)] = value      #5
        elif cell == 6:
            self.board[self.td_in_l(x, y + 1)] = value          #6
        elif cell == 7:
            self.board[self.td_in_l(x + 1, y + 1)] = value      #7

    def get_freecell(self, x, y):
        """ Функция получения координат свободной ячейки вокруг бота. """

        overview = self.get_overview(x, y)
        for loop in range(0, len(overview)):

            # На данный момент выбор пустой клетки не случайный...
            # СДЕЛАТЬ СЛУЧАЙНЫМ.
            freecell = False

            if overview[loop] == settings.EMPTY:
                if loop == 0:
                    x -= 1
                    y -= 1
                elif loop == 1:
                    y -= 1
                elif loop == 2:
                    x += 1
                    y -= 1
                elif loop == 3:
                    x -= 1
                elif loop == 4:
                    x += 1
                elif loop == 5:
                    x -= 1
                    y += 1
                elif loop == 6:
                    y += 1
                elif loop == 7:
                    x += 1
                    y += 1
                freecell = True
                break
        
        return x, y, freecell
        
    def random_board(self):
        """ Оставил ради ТЕСТА !!! Временный генератор рендомной картинки. """
        
        self.board = [random.randint(100, 999) for loop
                      in range(0, self.board_width * self.board_height)]