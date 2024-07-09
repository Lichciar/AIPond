# AIPond
My version of genetic algorithm

v. 0.1.2:
---------
    Планирование:
    3. Сделать вывод в консоль опциональной функцией.
    4. Добавить информационное меню: какие геномы сейчас живы и сколько их представителей.
    5. Добавить информационное меню: номер хода.
    6. Если директория "genotype" в корне отсутствует, то скрипт не запустится -- решить!
    7. Разработать дизайн для ботов: наверное, 8х8 точек. По кнопке на меню должно происходить переключение дизайна:
      7.1. Номер или цвет генотипа.
      7.2. Текущее действие бота, то которое он осуществил на данном шаге.

    Примечание:
    1. Скрипт работает очень медленно даже на i5. А загрузка 20%, я так понимаю одного ядра.
    2. Файлы с генотипами, это ещё тот геморой: удалять потом.....
    3. Возможно стоит рассмотреть работу скрипта в БД. БД ведь можно и на другом компе организовать.
       С БД потом проще вынимать информацию. Можно инфу вынать через небольшой сайтик.

    Выполнено:
    1. Добавлена инициализация x и y в функции board.get_freecell.
    2. Функция board.get_freecell переписана таким образом, чтобы
       выбор места для новой клетки осуществлялся случайным образом.
    3. Произведена небольшая корректировка комментариев.
    4. Введён контроль версии settings.py.
    5. Наконец-то запущена ГЛУПАЯ мутация.
    6. Подправлена защита от переполнения ботов.
    7. Добавлена новая система фиксирования информации "info",
       событий для скриптов. На данный момент она всё выводит в
       консоль.
    8. Класс bot.Bot.__init__ подлючен к "info".

v. 0.1.1:
---------
    1. Реализован минимальный набор комманд для ботов.
       Рождаются, живут, умирают.
    2. В данной версии отключены мутации в новые геномы,
       так сказать "глупая мутация".
    3. Рождение нового бота происходит не в случайном порядке,
       а по определённому алгоритму.

v. 0.1.0:
---------
    1.Создать прототип бота, который будет двигаться в хаотическом
      порядке по полю, теряя один процент жизни за ход, до тех пор,
      пока жизнь его не станет равна нулю.