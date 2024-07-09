#!/usr/bin/env python3

# --------------- комментарий 72 символа -------------------------------
# ----------------------- код 79 символов -------------------------------------

"""Задание:

Скрипт-класс генотипа.
0(1) - ничего не делать;
1(2) - повернуть в сторону (остаток от х/8);
            0-1-2
            3---4
            5-6-7
2(2) - движение в сторону (остаток от х/8);
3(2) - съесть впреди стоящего, если он (остаток от х/8 [другой веган,
       свой веган, другой минеральшик, свой минеральшик, другой хишник,
       свой хишник, минерал, биомасса]);
4(1) - фотосинтез;
5(1) - конец программы;

Начало: 19 июля 2019 г. 15:56 (версия 0.1.1.).
Обновлена: 15 августа 2022 г. 16:00.
"""

# Версия скрипта.
version = '0.1.2'

# Планирование разработки:

# Выполнено в ver.0.1.1 от 19 июля 2019 г.:
# ------------------------------------------
# 1. Создан новый класс Genotype в отдельном файле.
# 2. Сделана генерация нового генотипа.
# 3. Сделано тестирование генерации нового генотипа.
# 4. Сделана глупая мутация.
# 5. Сделано тестирование генерации мутированного генотипа.
# 6. Сделана сквозная нумерация генотипа.
# 7. Исправлена ОШИБКА: команда "5" не учитывается в длине генотипа.
# 8. Genotype и его CNG сохраняется в директории "./genotype/*.json".
# 9. Исправлена ОШИБКА: вывод на консоль трёх быйтных команд.
# 10. Исправлена ОШИБКА: если в генотипе не встречается команда "5",
#     слово "end" на консоль не выводится.
# 11. Добавил программу генотипа. ДОПИЛИТЬ.
# 12. Заменил слово "map" на "overview".
# 13. Добавлена функция "load" для чтения генотипа из файла.

# Выполнено в ver.0.1.2:
# -----------------------
# 1. Небольшая правка комментариев.
# 2. Добавлена система фиксирования информации "info".
# 3. 

# План работ на ver.0.1.X:
# --------------------------
# 1. Вывод ошибок в лог-файл (Нужно создать отдельный пакет).
# 2. Исправить глупую мутацию, а именно:
#    Допусти в программе генотипа №0 записана команда №1 с
#    параметром 34. В результате мутации программа генотипа №0
#    перезаписывается на комманду №0, а параметр 34 остаётся.
#    Команды с номером №34 не существует. Что делать? Просто игнорировать?
#    Или переписывать генотип с удалением параметра 34.
# 3. Рассмотреть возможность хранения информации о количестве
#    особей генотипа, относительной дате создания генотипа и
#    относительной дате смерти всех особей генотипа.
# 4. Ввиду вышесказанного пересмотреть процедуру "save":
#    может быть сделать две ("save" и "re-save"), либо передавать
#    в процедуру аргументы ("New" и "Alive")?
# 5. Рассмотреть возможность создание генотипа из файла, путём
#    передачи имени файла с генотипом.
# 6. Или добавить новые команды, или упростить генерацию генотипа.
# 7. Выбор направления по остатку от деления сделать функцией.
# 8. Определиться со значением на карте: 0 - пусто, 1 - стена, 2 и т.д.
#    значит уже номер бота.

import random   # Подключаем модуль генератора случайных чисел.
import json     # Подключаем модуль JSON.
import settings # Подключаем настройки.
import info     # Подключаем систему фиксирования работы скрипта.

# Создаём класс генотипа бота.
class Genotype:
    """ Класс, описывающий определённый генотип бота. """
    
    def __init__(self, operation = 'New', old_genotype = []):
        """ Конструктор класса. """
        
        # Вывод работы инициализации класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'genotype.Genotype.__init__'
        # Вывод информации.
        message = 'Инициализация нового экземпляра класса Genotype:'
        info.output(info_object, message)
        # Наименование операции над генотипом.
        message = ('_Наименование операции над генотипом (operation): ' +
            operation)
        info.output(info_object, message)
        
        # Инициализация порядкового номера генотипа.
        self.cng = settings.CNG_DEFAULT
        message = ('_Инициализация номера генотипа по умолчанию (cng =' +
            ' CNG_DEFAULT): ' + str(self.cng))
        info.output(info_object, message)
        
        # Инициализация пустого генотипа.
        self.genotype = [0 for loop in range(0, 64)]
        message = ('_Создание чистой программмы генотипа (genotype): ' +
            str(self.genotype))
        info.output(info_object, message)
        
        # Если нужно создать новый генотип...
        if operation == 'New':
            loop = 0
            while(loop < len(self.genotype)):
                
                # Записыпаев команду в генотип.
                self.genotype[loop] = random.randint(0, 5)
                message = ('_Случайная генерация команды №' + str(loop) +
                    ' для программы генотипа: команда №' +
                    str(self.genotype[loop]))
                info.output(info_object, message)
                                
                # Если записывается команда 5 - "конец программы",
                # останавливаем генерацию генотипа.
                if self.genotype[loop] == 5:
                    message = ('_Команда №5, означает конец программы.')
                    info.output(info_object, message)
                    break
                    
                # Комманды 1, 2, 3 имеют параметр.
                if (self.genotype[loop] >= 1
                   and self.genotype[loop] <= 3 and loop < 63):
                    loop += 1
                    self.genotype[loop] = random.randint(1, 64)
                    message = ('_Случайная генерация параметра для команды: ' +
                        str(self.genotype[loop]))
                    info.output(info_object, message)
                    
                loop += 1
                    
        # Если надо сделать генотип на основе существующего
        # мутированием.....
        # ГЛУПАЯ МУТАЦИЯ. ПЕРЕДЕЛАТЬ.
        # мутация не учитавает комманды с параметрами!!!
        if operation == 'Mutation':
            self.genotype = old_genotype
            message = ('_Получаем генотип родитель (old_genotype): ' +
                str(old_genotype))
            info.output(info_object, message)
            mutation = random.randint(0, 64)
            loop = random.randint(0, 63)
            message = ('_Производим мутацию программы генотипа №' +
                str(loop) + ' на команду №' + str(mutation))
            info.output(info_object, message)
            self.genotype[loop] = mutation

        message = ('_Мутированная программа генотипа (genotype): ' +
            str(self.genotype))
        info.output(info_object, message)
    
    def save(self):
        """ Сохранение генотипа на компьютер. """
        
        # Вывод работы метода класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'genotype.Genotype.save'

        # Открываем файл для присвоения порядкового номера.
        message = ('_Пытаемся открыть файл ' +
            str(settings.CNG_FILE) + ' для чтения')
        info.output(info_object, message)
        try:
            file = open(settings.CNG_FILE, 'r')
        # Если файл не существует
        except FileNotFoundError:
            # Current Number Genotype == cng.
            cng = settings.CNG_DEFAULT
            message = ('_Файл ' + str(settings.CNG_FILE) + ' не найден, ' +
                'поэтому cng = ' + str(cng))
            info.output(info_object, message)

        # Если файл открылся берём номер из него.
        else:
            cng = file.read()
            # Рассматриваем ситуацию когда файл существует,
            # пустой.
            if len(cng) == 0:
                cng = settings.CNG_DEFAULT
                message = ('_Файл ' + str(settings.CNG_FILE) + ' открылся, ' +
                    'но он пуст, поэтому cng = ' + str(cng))
                info.output(info_object, message)
            # Рассматриваем ситуацию когда в файле записано не
            # целое число.
            try:
                cng = int(cng)
            except ValueError:
                cng = settings.CNG_DEFAULT
                message = ('_Файл ' + str(settings.CNG_FILE) + ' открылся, ' +
                    'но содержит не цифровой номер, поэтому cng = ' +
                    str(cng))
                info.output(info_object, message)

            # Закрываем файл.
            file.close()
            message = ('_Файл ' + str(settings.CNG_FILE) + ' закрываем.')
            info.output(info_object, message)
        
        # Выдаём генотипу собственный номер.
        self.cng = cng

        # Увеличиваем порядковый номер на 1.
        cng += 1
        
        # Записываем новый номер в файл.
        message = ('_Пытаемся открыть файл ' + str(settings.CNG_FILE) +
            ' для записи')
        info.output(info_object, message)
        file = open(settings.CNG_FILE, 'w')
        file.write(str(cng))
        message = ('_Записываем в файл ' + str(settings.CNG_FILE) +
            ' cng увеличенный на 1')
        info.output(info_object, message)
        file.close()
        message = ('_Файл ' + str(settings.CNG_FILE) + ' закрываем.')
        info.output(info_object, message)
        
        # Сохраняем файл с генотипом в формате json.
        output_data = { 'cng': self.cng,
                        'genotype': self.genotype}
        
        # Открываем новый файл и записываем в него генотип.
        file = open(settings.GD_FILE + str(self.cng) + '.json', 'w')
        message = ('_Пытаемся открыть файл ' + str(settings.GD_FILE +
            str(self.cng) + '.json') + ' для записи')
        info.output(info_object, message)
        json.dump(output_data, file)
        message = ('_В файл ' + str(settings.GD_FILE + str(self.cng) +
            '.json') + ' записываем cng = ' + str(self.cng) + ' и генотип: ' +
            str(self.genotype))
        info.output(info_object, message)
        file.close()
        message = ('_Файл ' + str(settings.GD_FILE + str(self.cng) +
            '.json') + ' закрываем.')
        info.output(info_object, message)

    def load(self, cng):
        """ Чтение генотипа с компьютер. """
        
        # Вывод работы метода класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'genotype.Genotype.load'

        # Открываем файл для присвоения порядкового номера.
        message = ('_Пытаемся открыть файл ' + str(settings.GD_FILE +
            str(cng) + '.json') + ' для чтения')
        info.output(info_object, message)

        try:
            file = open(settings.GD_FILE + str(cng) + '.json', 'r')
        # Если файл не существует
        except FileNotFoundError:
            # Выводим в консоль сообщение об ошибке.
            message = ('_Файл ' + str(settings.GD_FILE) + str(cng) +
                '.json не существует.')
            info.output(info_object, message)
        # Если всё в порядке, читаем файл...
        else:
            input_data = file.read()
            # Если файл пустой, сообщаем об этом. И больше ничего....
            if len(input_data) == 0:
                message = ('_Файл ' + str(settings.GD_FILE) + str(cng) +
                    '.json пустой.')
                info.output(info_object, message)
            # Закрываем файл.
            file.close()
            message = ('_Файл ' + str(settings.GD_FILE) + str(cng) +
                    '.json закрыт.')
            info.output(info_object, message)

        self.cng = json.loads(input_data)['cng']
        self.genotype = json.loads(input_data)['genotype']
        message = ('_Из файла ' + str(settings.GD_FILE) + str(cng) +
            '.json получено: cng = ' + str(self.cng) + ', genotype = [' +
            str(self.genotype) + ']')
        info.output(info_object, message)
        
    def program(self, ps, direction, x, y, health, number, overview = []):
        """ Программа генотипа.
            (ps == Program Step). """

        # Вывод работы метода класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'genotype.Genotype.program'
        
        # Инициализируем переменную.
        message = ''

        # Код "0" = "Ничего не делаю."
        if self.genotype[ps] == 0 or self.genotype[ps] > 5:
            message = ('Ничего не делаю!')
            ps += 1

        # Код "1" = "Поворачиваюсь в сторону."
        # 0-1-2
        # 3---4
        # 5-6-7
        elif self.genotype[ps] == 1:
            direction = self.genotype[ps+1]%8
            message = ('Повернул в сторону!')
            ps += 2
            
        # Код "2" = "Двигаюсь в сторону."
        # 0-1-2
        # 3---4
        # 5-6-7
        elif self.genotype[ps] == 2:

            if (ps < 63 and self.genotype[ps+1]%8 == 0 and
                self.overview_check('Move', 'NW', overview)):
                x -= 1;
                y -= 1;
                message = 'Двигаюсь на северо-запад!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 1 and
                self.overview_check('Move', 'N', overview)):
                y -= 1;
                message = 'Двигаюсь на север!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 2 and
                self.overview_check('Move', 'NE', overview)):
                x += 1;
                y -= 1;
                message = 'Двигаюсь на северо-восток!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 3 and
                self.overview_check('Move', 'W', overview)):
                x -= 1;
                message = 'Двигаюсь на запад!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 4 and
                self.overview_check('Move', 'E', overview)):
                x += 1;
                message = 'Двигаюсь на восток!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 5 and
                self.overview_check('Move', 'SW', overview)):
                x -= 1;
                y += 1;
                message = 'Двигаюсь на юго-запад!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 6 and
                self.overview_check('Move', 'S', overview)):
                y += 1;
                message = 'Двигаюсь на юг!'

            elif (ps < 63 and self.genotype[ps+1]%8 == 7 and
                self.overview_check('Move', 'SE', overview)):
                x += 1;
                y += 1;
                message = 'Двигаюсь на юго-восток!'
            
            # Увеличиваем шаг программы.
            ps += 2
            
        # Код "3" = "Съедаю впереди стоящего, если он..."
        # 0-1-2
        # 3---4
        # 5-6-7
        elif self.genotype[ps] == 3:
            message = 'Съедаю впереди стоящего, если он...'
            if not(overview[direction] == settings.EMPTY or
                overview[direction] == settings.WALL):
                health += 50
                overview[direction] = settings.EMPTY
                message += ' перед моим лицом. Приятного апетита!'
            ps += 2
            
        # Код "4" = "Фотосинтез."
        elif self.genotype[ps] == 4:
            message = 'Фотосинтез!'
            health += 10
            ps += 1
            
        # Код "5" = "Конец программы генотипа."
        elif self.genotype[ps] == 5:
            message = 'Конец программы генотипа!'
            ps = 0
        
        # Выводим на экран консоли действие бота.
        if message:
            message = ('Бот №' + str(number) + ' - генотип №' + str(self.cng) +
                ' (' + str(x) + ', ' + str(y) + ') - ' + message +
                ' Ячейка памяти №' + str(ps) + '.')
            info.output(info_object, message)

        # Проверяем не закончилась ли программа.
        if ps >= 63:
            ps -= 63
        
        # В конце хода отнимаем 1% жизни.
        health -= 1
        
        # Возвращаем изменённые параметры бота.
        return ps, direction, x, y, health, overview
    
    def overview_check(self, operation, direction, overview = []):
        """ Проверяем пространство вокруг бота. """

        # Проверяем пространство для передвижения
        # 0-1-2
        # 3---4
        # 5-6-7

        # Вывод работы метода класса:
        # Название служебной программы,
        # которая запрашивает вывод информации.
        info_object = 'genotype.Genotype.overview_check'

        if operation == 'Move':
            Answer = False

            if (direction == 'NW' and overview[0] == settings.EMPTY or
                direction == 'N' and overview[1] == settings.EMPTY or
                direction == 'NE' and overview[2] == settings.EMPTY or
                direction == 'W' and overview[3] == settings.EMPTY or
                direction == 'E' and overview[4] == settings.EMPTY or
                direction == 'SW' and overview[5] == settings.EMPTY or
                direction == 'S' and overview[6] == settings.EMPTY or
                direction == 'SE' and overview[7] == settings.EMPTY):
                Answer = True
            else:
                message = 'Движение в сторону не возможно - клетка занята.'
                info.output(info_object, message)
            return Answer
        
    def console_output(self):
        """ Выводим генотип на экран консоли. """

        # ДОПИЛИТЬ.
        # Подправить или совсем убрать эту функцию.
        loop = 0
        counter = True
        message = 'start -> '
        while(loop < len(self.genotype)):
            # Записыпаев команду в генотип.
            message += str(self.genotype[loop])
                                
            # Если записывается команда 5 - "конец программы",
            # останавливаем генерацию генотипа.
            if self.genotype[loop] == 5:
                message += ' -> '
                loop += 1
                break
                    
            # Комманды 1, 2, 3 имеют параметр.
            if (self.genotype[loop] >= 1
               and self.genotype[loop] <= 3 and loop < 63
               and counter):
                message += '-'
                loop += 1
                counter = False
                continue
            
            counter = True
            message += ' -> '
            loop += 1
        
        message += 'end'
        print(message)
        print('Длина генотипа равняется', loop, 'из', len(self.genotype), '.\n')

# Тестирование класса.
if __name__ == '__main__':
    
    # Приветствие.
    print('Запущено тестирование класса Genotype v.', version, '.')
    print('Справка: CNG = Current Number Genotype. \n')
    
    # Создаём новый генотип b.
    b = Genotype('New')
    b.save()
    print('Создаём новый генотип CNG =', b.cng, ':')
    # Выводим генотип b на экран.
    b.console_output()
    
    # Делаем мутацию генотипа b.
    c = Genotype('Mutation', b.genotype)
    c.save()
    print('Создаём генотип CNG =', c.cng, '(мутацию генотипа CNG =', b.cng, '):')
    # Выводим генотип с на экран.
    c.console_output()
    
    # Проводим множественную мутацию.
    loop = 50

    print('Производим множественную мутацию генотипа CNG =', c.cng, ':')    
    while(loop > 0):
        # Делаем мутацию генотипа c.
        c = Genotype('Mutation', c.genotype)
        c.save()
        loop -= 1
    
    # Выводим генотип с на экран.
    print('Оконечная мутация - генотип CNG =', c.cng, ':')  
    c.console_output()

    # Создаём новый генотип d.
    d = Genotype('New')
    # ... и загружаем в него генотип b.
    d.load(b.cng)
    d.save()
    print('Создаём генотип CNG =', d.cng,
        '(загруженный генотип CNG =', b.cng, '):')
    # Выводим генотип d на экран.
    d.console_output()

    # Проверяем совпадение генотипа c и d.
    # Проверяем каждый элемент генотипа.
    counter = 0
    for loop in range(0, 64):
        if not(c.genotype[loop] == d.genotype[loop]):
            counter += 1
    
    if counter > 0:
        print('Выявлено', counter, 'различий генотипа CNG =',
            c.cng, 'и генотипа CNG =', d. cng, '.\n')
    else:
        print('Различий генотипа CNG =', с.cng, 'и генотипа CNG =',
            d. cng, ' не выявлено.\n')
    
    # Тест программы генотипа.
    print('Производим тестирование программы генотипа CNG =', c.cng, ':')
    health = x = y = 10
    direction = 0
    loop = 0
    number = 666
    overview = [2 for loop in range(0, 8)]
    while health > 0:
        [loop, direction, x, y, health, overview] = d.program(loop, direction, x, y,
            health, number, overview)
        print('ps =', loop, 'direction =', direction ,'x =', x, ', y =',
            y, ' ,health =', health, 'overview =', overview)