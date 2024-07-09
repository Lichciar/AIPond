#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс окружения для ботов.
Начало: 17 апреля 2018 г. 01:23.
Обновлена: 26 июня 2022 г. 18:56.

"""

# Версия скрипта.  
version = '0.1.2'

# Планирование разработки:

# Выполнено в ver.0.1.0:
# -----------------------
# 1. Создан прототип окружающей среды.

# Выполнено в ver.0.1.1 от 19 августа 2019 г. :
# ----------------------------------------------
# 1. Добавлена функция get_map.
 
# Выполнено в ver.0.1.2:
# ------------------------
# 1. Добавлена инициализация x и y в функции get_freecell.
# 2. Функция get_freecell переписана таким образом, чтобы выбор места
#    для новой клетки осуществлялся случайным образом.
# 3. Произведена небольшая корректировка комментариев.
# 4. Удалена функция random_board.
# 5. Добавлена система фиксирования информации "info".

# План работ на ver.0.1.X:
# ------------------------
# 1. Добавить включаемое логирование/вывод в консоль информации
#    о работе функций.

import settings # Подключаем настройки.
import info     # Подключаем систему фиксирования работы скрипта.
import random   # Подключаем модуль генератора случайных чисел.

class Enviroment:
    """ Класс описывающий окружающую среду бота. """
    
    def __init__(self, width = 16, height = 16):
        """ Конструктор класса. Создаёт двухмерный мир. """
        
        # Ширина мира.
        self.board_width = width
        # Высота мира.
        self.board_height = height
        
        # Заполняем пустыми клетками весь мир.
        self.board = [settings.EMPTY for loop
                      in range(0, self.board_width * self.board_height)]
        # Заполняем другим цветом границы мира:
        # левую и правую,
        for loop in range(0, self.board_width):
            self.board[loop] = settings.WALL
            self.board[loop + ((self.board_height - 1) *
                self.board_width)] = settings.WALL
        # верхнюю и нижнюю.
        for loop in range(0, self.board_height):
            self.board[loop * self.board_width] = settings.WALL
            self.board[loop * self.board_width +
                self.board_width - 1] = settings.WALL

        # Вывод работы инициализации класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'board.Enviroment.__init__'
        # Вывод информации.
        message = 'Инициализация нового экземпляра класса Enviroment:'
        info.output(info_object, message)
        message = '_Ширина мира (board_width): ' + str(self.board_width)
        info.output(info_object, message)
        message = '_Высота мира (board_height): ' + str(self.board_height)
        info.output(info_object, message)
        message = ('_Мир ограничен границами (WALL) сверху, снизу,' +
                  'слева и справа.')
        info.output(info_object, message)

    def td_in_l(self, x, y):
        """ Функция перевода декартовых координат в индекс списка.
        (примечание: от TwoDimensions_in_List)."""
        
        # Вывод работы функции:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'board.Enviroment.td_in_l'
        # Вывод информации.
        message = 'Перевод декартовых координат в индекс списка:'
        info.output(info_object, message)
        message = ('_Координаты ' + str(x) + ', ' + str(y) +
             ' (x, y) = индекс списка №' +
             str(self.board_width * (y - 1) + x - 1))
        info.output(info_object, message)

        return (self.board_width * (y - 1) + x - 1)

    def get_overview(self, x, y):
        """ Функция получения обзора в одну клетку вокруг бота. """

        # 0-1-2
        # 3---4
        # 5-6-7
        # Инициализация списка обзора.
        overview = []

        # Вывод работы функции:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'board.Enviroment.get_overview'
        # Вывод информации.
        message = 'Функция получения обзора в одну клетку вокруг бота:'
        info.output(info_object, message)
        message = '_Координаты бота (x, y): ' + str(x) + ', ' + str(y)
        info.output(info_object, message)

        # Получение обзора.
        overview.append(self.board[self.td_in_l(x - 1, y - 1)]) #0
        overview.append(self.board[self.td_in_l(x, y - 1)])     #1
        overview.append(self.board[self.td_in_l(x + 1, y - 1)]) #2
        overview.append(self.board[self.td_in_l(x - 1, y)])     #3
        overview.append(self.board[self.td_in_l(x + 1, y)])     #4
        overview.append(self.board[self.td_in_l(x - 1, y + 1)]) #5
        overview.append(self.board[self.td_in_l(x, y + 1)])     #6
        overview.append(self.board[self.td_in_l(x + 1, y + 1)]) #7

        message = '_Обзор вокруг бота (overview): ' + str(overview)
        info.output(info_object, message)

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

        # Вывод работы функции:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'board.Enviroment.set_overview'
        # Вывод информации.
        message = ('Функция изменения окружающей среды в одну клетку вокруг' +
            ' бота:')
        info.output(info_object, message)
        message = ('_0-1-2')
        info.output(info_object, message)
        message = ('_3---4')
        info.output(info_object, message)
        message = ('_5-6-7')
        info.output(info_object, message)
        message = ('_Меняем обзорную клетку (cell): ' + str(cell) )
        info.output(info_object, message)
        message = ('_С центром обзора (x, y): ' + str(x) + ', ' +str(y))
        info.output(info_object, message)
        message = ('_На значение (value): ' + str(value))
        info.output(info_object, message)

    def get_freecell(self, x = 0, y = 0):
        """ Функция получения координат свободной ячейки около бота. """

        # Вывод работы функции:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'board.Enviroment.get_freecell'
        # Вывод информации.
        message = 'Функция получения координат свободной ячейки около бота:'
        info.output(info_object, message)

        # Собираем информацию о занятости места вокруг бота.
        overview = self.get_overview(x, y)
        # Инициализируем пустой массив для номеров клеток
        freecell_array = []
        # Индикатор наличия хотя бы одной свободной клетки вокруг бота.
        # False - свободные клетки отсутствуют. True - свободные клетки
        # присутствуют.
        freecell = False

        for loop in range(0, len(overview)):

            # Собираем массив с "направлениями",
            # в которых расположенны пустые клетки.
            if overview[loop] == settings.EMPTY:
                freecell_array.append(loop)

        # Если есть пустые клетки, то выбираем среди них.
        if freecell_array:

            # Выбираем случайный индекс в пуле свободных клеток.
            freecell_random = random.randint(0,
                len(freecell_array) - 1)

            # Присваиваем координаты перемещения согласно "направлению":
            if freecell_array[freecell_random] == 0:
                x -= 1
                y -= 1
            elif freecell_array[freecell_random] == 1:
                y -= 1
            elif freecell_array[freecell_random] == 2:
                x += 1
                y -= 1
            elif freecell_array[freecell_random] == 3:
                x -= 1
            elif freecell_array[freecell_random] == 4:
                x += 1
            elif freecell_array[freecell_random] == 5:
                x -= 1
                y += 1
            elif freecell_array[freecell_random] == 6:
                y += 1
            elif freecell_array[freecell_random] == 7:
                x += 1
                y += 1

            freecell = True

            message = ('_Список пустых клеток около бота (freecell_array): ' +
                str(freecell_array))
            info.output(info_object, message)
            message = ('_Выбор пал на пустую клетку (freecell_array' +
                '[freecell_random]) = ' +
                str(freecell_array[freecell_random]))
            info.output(info_object, message)
            message = ('_Пустая клетка около бота есть (freecell) = ' +
                str(freecell))
            info.output(info_object, message)
        
        # Если пустые клетки отсутствуют, то об этом тоже сообщаем.
        if freecell == False:
            message = ('_Пустые клетки около бота отсутствуют ' + 
                '(freecell_array):' + str(freecell_array))
            info.output(info_object, message)

        return x, y, freecell