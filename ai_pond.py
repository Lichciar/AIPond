#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт иллюстрирующий генный алгоритм.
Начало: 28 марта 2018 г. 00:16.
Обновлена: 28 июня 2024 г. 14:10.

"""

# Версия скрипта.  
version = '0.1.2'

# Планирование разработки:

# Выполнено в ver.0.1.0:
# -----------------------
# 1.Создал прототип окна с рабочей графической областью,
#   заполняющееся квадратами случайного цвета.
# 2.Запустить графическую оболочку.
# 3.Создать класс поля.
# 4.Создать класс экземпляра AI.
# 5.Генотип смотрим в файле.

# Выполнено в ver.0.1.1 от 31 июля 2020 г.:
# -------------------------------------------
# 1. Собрать с новым классом Genotype.
# 2. Первая более или менее рабочая версия.

# Выполнено в ver.0.1.2 от 28 июня 2024 г.:
# ----------------------
# 1. Добавлен контроль версии скрипта-настройки settings.py.
# 2. Небольшие правки комментариев.
# 3. Настроена ГЛУПАЯ мутация генотипов.
# 4. Проверка на переполнение ботов привязана к количеству клеток.
# 5. Подключена служба фиксации информации "info".
#    Требуется её настройка.
# 6. Скрипт теперь выводит всю слуужебную информацию через класс info.

# План работ на ver.0.1.X:
# ----------------------

import settings # Подключаем настройки.
import info     # Подключаем систему фиксирования работы скрипта.
import bot      # Подключаем класс искуственного интелекта.
import genotype # Подключаем класс искуственного интелекта.
import board    # Подключаем класс окружающей среды.
import json     # Подключаем модуль JSON.
import tkinter  # Подключаем модуль GUI/API - Tk.
import random   # Подключаем модуль генератора случайных чисел.

# Описываем переменные.
bot_array = []                      # Массив ботов.
number = settings.NUMBER_DEFAULT    # Индивидуальный номер бота.

# Создаём мир в котором будут жить боты.
main_board = board.Enviroment(settings.CELL, settings.CELL)
main_window = tkinter.Tk()

# В качестве названия окна используем название скрипта
# и его текущая версия.
main_window.title('AIPond v. ' + version)

# Вывод работы инициализации скрипта:
# Название служебной программы,
# которая запрашивает вывод информации.
info_object = 'ai_pond.__main__'
# Вывод информации.
message = 'Версия бота: ' + bot.version
info.output(info_object, message)
message = 'Версия генотипа: '+ genotype.version
info.output(info_object, message)
message = 'Версия окружающего мира для ботов: ' + board.version
info.output(info_object, message)
message = 'Версия настроек: ' + settings.version
info.output(info_object, message)
message = 'Версия системы фиксации информации: ' + info.version
info.output(info_object, message)

# Создаём среду в которой будут жить боты.
pond = tkinter.Canvas(main_window, width=settings.WIDTH,
    height=settings.HEIGHT)
pond.pack()

# Создаём стартовые генотипы для ботов (10 штук)
# и первых ботов.
for loop in range(0, 10):
    bot_genotype = genotype.Genotype('New')
    bot_genotype.save()
    bot_array.append(bot.Bot(cng = bot_genotype.cng, number = number))
    number += 1

# Помещаем начальных ботов в окружающую среду.
for loop in range(0, number - settings.NUMBER_DEFAULT):
    birth = True
    while birth:
        # Положение бота в мире по оси Х.
        x = random.randint(1, settings.CELL - 1)
        # Положение бота в мире по оси Y.
        y = random.randint(1, settings.CELL - 1)
        if (main_board.board[main_board.td_in_l(x, y)] == settings.EMPTY):
            # Передаём координаты рождения боту.
            bot_array[loop].x = x
            bot_array[loop].y = y
            # Передаём координаты расположения бота в окружающую среду.
            main_board.board[main_board.td_in_l(x, y)] = (loop +
                settings.NUMBER_DEFAULT)
            birth = False

# Создаём бесконечный цикл для ботов.
# (В будущем он должен быть всё таки конечным).
step = 0
while True:
    # Вывод работы бесконечного цикла скрипта:
    # Название служебной программы,
    # которая запрашивает вывод информации.
    info_object = 'ai_pond.__main__.step'
    # Вывод информаци.
    message = 'Ход № ' + str(step)
    info.output(info_object, message)

    # Перед каждым ходом очищаем список мёртвых ботов.
    rip = []
    
    # Перебираем всех ботов.
    for loop in range(len(bot_array)):
        
        # Если бот уже мёртв - берём следующего.
        if bot_array[loop].health <= 0:
            continue

        # Получаем зону обзора вокруг бота.
        overview_before = main_board.get_overview(bot_array[loop].x,
            bot_array[loop].y)

        # Определим генотип бота и откроем файл с генотипом
        # для чтение.
        bot_genotype.load(bot_array[loop].cng)
        
        # Создаём новый объект-список.
        overview_after = list(overview_before)

        # Исполняем код генотипа бота.
        [bot_array[loop].ps, bot_array[loop].direction, x_after,
            y_after, bot_array[loop].health, overview_after] = (
            bot_genotype.program(bot_array[loop].ps,
            bot_array[loop].direction, bot_array[loop].x,
            bot_array[loop].y, bot_array[loop].health,
            bot_array[loop].number, overview_after))

        # Если координаты бота изменились...
        if not(x_after == bot_array[loop].x and y_after == bot_array[loop].y):
            # По старым координатам клетку освобождаем.
            main_board.board[main_board.td_in_l(
                bot_array[loop].x, bot_array[loop].y)] = settings.EMPTY
            # По новым координатам клетку заполняем.
            bot_array[loop].x = x_after
            bot_array[loop].y = y_after
            main_board.board[main_board.td_in_l(
                bot_array[loop].x, bot_array[loop].y)] = (
                bot_array[loop].number)

        # Сравниваем overview_before и overview_after
        for loop_overview in range(0, len(overview_before) - 1):
            # Если находим различие...
            if not (overview_before[loop_overview] ==
                overview_after[loop_overview]):
                # Убиваем съеденого бота...
                rip.append(overview_before[loop_overview])
                # Название служебной программы,
                # которая запрашивает вывод информации.
                info_object = 'ai_pond.__main__'
                # Вывод информаци.
                message = ('Бот №' + str(overview_before[loop_overview]) +
                    ' был съеден.')
                info.output(info_object, message)

        # Если здоровье бота превысило 100%,
        # бот может сделать свою копию или нового бота с мутирующим
        # от себя генотипом.
        if bot_array[loop].health > 100:

            # Название служебной программы,
            # которая запрашивает вывод информации.
            info_object = 'ai_pond.__main__'
            # Вывод информаци.
            message = ('Бот №' + str(bot_array[loop].number) +
                ' пора плодиться!')
            info.output(info_object, message)
            bot_array[loop].health //= 2
            # Ищем поблизости свободную клетку.
            (new_x, new_y, freecell) = main_board.get_freecell(
                bot_array[loop].x, bot_array[loop].y)
            # Роллим на мутацию бота...
            mutatin_roll = random.randint(0, 100)
            # Если найдена пустая клетка и шанс на мутацию успешен,
            # то создаём нового бота с мутацией.
            if freecell and mutatin_roll <= settings.MUTATION_CHANCE:
                # Производим мутацию генотипа родителя.
                bot_mutation_genotype = genotype.Genotype('Mutation',
                    bot_genotype.genotype)
                # и сохраняем её...
                bot_mutation_genotype.save()
                # Добавляем бота с мутированным генотипом.
                bot_array.append(bot.Bot(x = new_x, y = new_y,
                    cng = bot_mutation_genotype.cng, number = number))
                main_board.board[main_board.td_in_l(new_x, new_y)] = number
                number += 1
                # Название служебной программы,
                # которая запрашивает вывод информации.
                info_object = 'ai_pond.__main__'
                # Вывод информаци.
                message = 'Появился новый генотип!'
                info.output(info_object, message)
            # Если найдена пустая клетка, но шанс на мутацию провален,
            # то создаём нового бота с геномом бота родителя.  
            elif freecell and mutatin_roll > settings.MUTATION_CHANCE:
                bot_array.append(bot.Bot(x = new_x, y = new_y,
                    cng = bot_array[loop].cng, number = number))
                main_board.board[main_board.td_in_l(new_x, new_y)] = number
                number += 1
            # В противном случае умираем.
            else:
                bot_array[loop].health = 0

        # Если бот умер в процессе выполнения программы,
        # удаляем его из мира.
        if bot_array[loop].health == 0:
            # Название служебной программы,
            # которая запрашивает вывод информации.
            info_object = 'ai_pond.__main__'
            # Вывод информаци.
            message = 'Бот №' + str(bot_array[loop].number) + '- Умер'
            info.output(info_object, message)
            rip.append(bot_array[loop].number)
            continue

    # Удаляем мёртвых ботов.
    # Название служебной программы,
    # которая запрашивает вывод информации.
    info_object = 'ai_pond.__main__.rip'
    # Вывод информаци.
    message = 'bot before ' + str(len(bot_array))
    info.output(info_object, message)
    message = rip
    info.output(info_object, message)
    for loop_rip in rip:
        for loop in range(0, len(bot_array)):
            if loop_rip == bot_array[loop].number:
                # Название служебной программы,
                # которая запрашивает вывод информации.
                info_object = 'ai_pond.__main__'
                # Вывод информаци.
                message = 'Удаляю бота №' + str(bot_array[loop].number)
                info.output(info_object, message)
                main_board.board[main_board.td_in_l(bot_array[loop].x,
                    bot_array[loop].y)] = settings.EMPTY
                del bot_array[loop]
                break
    # Название служебной программы,
    # которая запрашивает вывод информации.
    info_object = 'ai_pond.__main__.rip'
    # Вывод информаци.
    message = 'bot after' + str(len(bot_array))
    info.output(info_object, message)

    #ТЕСТ
    if (len(bot_array) > ((settings.CELL - 2) ** 2) or len(bot_array) < 2):
        while True:
            exit 

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
            if (main_board.board[main_board.td_in_l(loop_x, loop_y)] ==
                settings.EMPTY):
                color = settings.EMPTY_COLOR
            elif (main_board.board[main_board.td_in_l(loop_x, loop_y)] ==
                settings.WALL):
                color = settings.WALL_COLOR
            else:
                color = settings.BOT_COLOR
            pond.create_rectangle(x1, y1, x2, y2, fill = color)

    # Обновляем полотно.
    main_window.update()
    
    # Удаляем мёртвых ботов.
    for loop in range(len(bot_array)):
        if bot_array[loop].health == 0:
            main_board.board[main_board.td_in_l(bot_array[loop].x,
                bot_array[loop].y)] = settings.EMPTY

    # Делаем шаг.
    step += 1