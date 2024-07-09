#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-настройка для всего проекта.
Начало: 20 июня 2022 г. 22:32.
Обновлена: 15 августа 2022 г. 16:00.

"""

# Версия скрипта.  
version = '0.1.1'

# Планирование разработки:
 
# План работ на ver.0.1.1:
# ------------------------
# 1. Добавлен контроль версии скрипта:
#    Версия 0.1.0 была совсем простая, без коментарием и т.д.
# 2. Добавлен список INFO_PERMISSION для хранения разрешений на вывод
#	 сообщений в консоль или файл.

# План работ на ver.0.1.X:
# ------------------------

# Ширина.
WIDTH = 600
# Высота.
HEIGHT = 600
# Количество клеток
CELL = 60      
# Ширина одной клетки
WCELL = WIDTH // CELL
# Высота одной клетки
HCELL = HEIGHT // CELL
# Пустая ячейка.
EMPTY = 0
# Цвет пустой ячейки.
EMPTY_COLOR = '#000080'
# Стена.
WALL = 1
# Цвет стены.
WALL_COLOR = '#150'
# Цвет ботов.
BOT_COLOR = '#FF0000'
# Шанс мутации в процентах (max 100).
MUTATION_CHANCE = 30
# Файл хранения порядкового номера генотипа
# (Current Number Genotype == CNG).
# (W) Правильно ли стоит "КОСАЯ ЛИНИЯ"?
CNG_FILE = 'genotype/CNG.txt'
# Директория хранения генотипов
# (Genotype Directory == GD).
# (W) Правильно ли стоит "КОСАЯ ЛИНИЯ"?
GD_FILE = 'genotype/'
# Начальный номер для первого генотипа.
CNG_DEFAULT = 1
# Начальный номер для первого бота.
NUMBER_DEFAULT = 2
# Режим тестирования.
DEBUG = True

# Система фиксирования информации и событий:
# Создаём словарь ,где
# "console" - разрешение на вывод в консоль;
# "file" - разрешение на вывод в файл;
# что-то отличное от вышеописанного означает ЗАПРЕТ
# на трансляцию сообщений.
INFO_PERMISSION = {
	'info.__main__': 'none',
	'bot.Bot.__init__': 'none',
	'board.Enviroment.__init__': 'none',
	'board.Enviroment.td_in_l': 'none',
	'board.Enviroment.get_overview': 'none',
	'board.Enviroment.set_overview': 'none',
	'board.Enviroment.get_freecell': 'none',
	'genotype.Genotype.__init__': 'none',
	'genotype.Genotype.save': 'none',
	'genotype.Genotype.load': 'none',
	'genotype.Genotype.program': 'none',
	'genotype.Genotype.overview_check': 'none',
	'ai_pond.__main__': 'console',
	'ai_pond.__main__.step': 'console',
	'ai_pond.__main__.rip': 'none',}