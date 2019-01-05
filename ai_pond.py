#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт иллюстрирующий генный алгоритм.
Начало: 28 марта 2018 г. 00:16.
Обновлена: 14 сентября 2018 г. 02:59.

"""

# Версия скрипта.  
ai_pond_version = '0.1.0'

# Планирование разработки:

# Исправлено в ver.0.1.0:
# -----------------------
# 1.Создал прототип окна с рабочей графической областью,
#   заполняющееся квадратами случайного цвета.
#
# План работ на ver.0.1.X:
# ----------------------
# 1.Запустить графическую оболочку.
# 2.Создать класс поля.
# 3.Создать класс экземпляра AI.

# Подключаем настройки.
import settings

# Подключаем класс искуственного интелекта.
import bot

# Подключаем класс окружающей среды.
import board

# Подключаем модуль GUI/API - Tk.
import tkinter

# Подключаем модуль генератора случайных чисел.
import random

# Описываем константы.
genetic_number = 1  # Индивидуальный номер генотипа.
number = 0          # Индивидуальный номер бота.
genetic_bot = []    # Массив генетических типов ботов.ы
ai_bot = []         # Массив ботов.
bot_generation = 1  # Поколение ботов.

# Создаём мир в котором будут жить боты.
main_board = board.Enviroment(settings.CELL, settings.CELL)
main_window = tkinter.Tk()

# В качестве названия окна используем название скрипта
# и его текущая версия.
main_window.title('AIPond v.' + ai_pond_version)

print('Версия бота: ', bot.bot_version)
print('Версия окружающего мира для ботов:', board.board_version)

# Создаём среду в которой будет жить AI.
pond = tkinter.Canvas(main_window, width=settings.WIDTH,
    height=settings.HEIGHT)
pond.pack()

# Создаём первое поколение генотипов для ботов (10 штук).
# Привязку к цвету надо делать как-то по другому.
# Генотипы должны иметь имя.
genetic_bot.append(bot.Resident(genetic_number))
while number < 25:
    birth = True
    while birth:
        # Положение бота в мире по оси Х.
        pos_x = random.randint(1, settings.CELL - 1)
        # Положение бота в мире по оси Y.
        pos_y = random.randint(1, settings.CELL - 1)
        if (main_board.board[main_board.td_in_l(pos_x, pos_y)] ==
            settings.EMPTY):
            # ТЕСТ - вывод номер и декартовых координат.
            print (number, pos_x, pos_y)
            # Создаём ботов.
            ai_bot.append(bot.Resident(pos_x, pos_y, genetic_number, number))
            # Добавляем бота в среду обитания (мир).
            # У ботов одного генотипа должен быть один цвет.
            main_board.board[main_board.td_in_l(pos_x, pos_y)] = 500 + number
            birth = False
    number += 1

# Создаём бесконечный цикл для ботов.
# (В будущем он должен быть всё таки конечным).
step = 0
while True:
    print('Ход №' + str(step))
    # Делаем шаг в программе бота.
    for loop in range(len(ai_bot)):
        
        # Если бот уже мёртв - не работаем с ним.
        if ai_bot[loop].health > 0:
            ai_bot[loop].program()
        else:
            continue
        
        # Если бот умер в процессе выполнения программы,
        # удаляем его из мира.
        if ai_bot[loop].health == 0:
            print('Бот №', ai_bot[loop].number,
                '- Умер.', loop)
            continue
        
        # Делаем анализ работы бота.
        temp_x = ai_bot[loop].pos_x + ai_bot[loop].pos_dx
        temp_y = ai_bot[loop].pos_y + ai_bot[loop].pos_dy
        # Защита от перехода границы.
        # (Возможно не понадобится).
        if temp_x < 0:
            temp_x = 0
        if temp_y < 0:
            temp_y = 0
        
        # Если в точке перехода пусто, идём туда.
        if (main_board.board[main_board.td_in_l(temp_x, temp_y)] ==
            settings.EMPTY):
            main_board.board[main_board.td_in_l(ai_bot[loop].pos_x,
                ai_bot[loop].pos_y)] = settings.EMPTY
            ai_bot[loop].pos_x = ai_bot[loop].pos_x + ai_bot[loop].pos_dx
            ai_bot[loop].pos_y = ai_bot[loop].pos_y + ai_bot[loop].pos_dy
            main_board.board[main_board.td_in_l(temp_x,
                temp_y)] = 500 + ai_bot[loop].number
      
    # Делаем отрисовку мира.
    # Делать прорисовку только изменившихся частей.
    # не рисовать пустые клетки и края.
    pond.delete('all')
    for loop_y in range(1, main_board.board_height + 1):
        for loop_x in range(1, main_board.board_width + 1):
            x1 = (loop_x - 1) * settings.WCELL
            y1 = (loop_y - 1) * settings.HCELL
            x2 = (loop_x - 1) * settings.WCELL + settings.WCELL
            y2 = (loop_y - 1) * settings.HCELL + settings.HCELL
            # Отрисовываем цветными квадратами мир.
            color = main_board.board[main_board.td_in_l(loop_x, loop_y)]
            pond.create_rectangle(x1, y1, x2, y2, fill = '#' + str(color))

    # Обновляем полотно.
    main_window.update()
    
    # Удаляем мёртвых ботов.
    for loop in range(len(ai_bot)):
        if ai_bot[loop].health == 0:
            main_board.board[main_board.td_in_l(ai_bot[loop].pos_x,
                ai_bot[loop].pos_y)] = settings.EMPTY
                
    
    # Делаем шаг.    
    step += 1