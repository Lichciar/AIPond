# Ширина.
WIDTH = 400
# Высота.
HEIGHT = 400
# Количество клеток
CELL = 10       
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
# Шанс мутации в процентах.
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