import main_txt_function as fn
from functools import reduce
import clear as cl
import time



def second_menu():
    while True:
        cl.clear_screen()
        print('Автопарк\n')
        print('Список команд:')
        ch = input('1 - Поиск по фамилии\n2 - Поиск по id\n3 - Поиск по № маршрута\n'\
                    '4 - Возврат в основное меню\n\nВведите номер команды ->:')
        if ch == '1':
            search_surname()
        if ch == '2':
            search_id()
        if ch == '3':
            route_number_search()
        if ch == '4':
            print('Куда же Вы...')
            time.sleep(1)
            return


def search_surname():
    print('не реализовал, пока..')
    time.sleep(1)
    # search_surname_data('route.txt')

def search_id():
    search_id_data() # поиск по id водителя.

def route_number_search():
    route_number_search_data() # поиск по номеру маршрута.



def route_number_search_data(): # поиск по номеру маршрута.
    while True:
            cl.clear_screen()
            route_list = fn.reading_from_file('route.txt') # получение данных из таблицы route.txt
            route_list_len = len(route_list) # узнал количество вложений в списке
            out_list = []
            count = 0
            route = input('Нажмите ENTER для возврата в меню,\nИЛИ введите номер маршрута ->:')
            if route == '':
                return # выводит для повтора ввода маршрута
            for i in range(len(route_list)):
                count +=1 # считаю количество проходов, списков в списке
                temp_list_route = []
                for j in route_list[i]:
                    temp_list_route.append(j) # раскрываю внутренние списки, каждое вложение в начальном списке.
                if temp_list_route[4] == route: # если на позиции маршрут из входящих данных совпадает с введенным, то строка 57.
                    id = temp_list_route[0] # находим и сохраняем id водителя из найденного по номеру маршрута,
                                            # верного, нужного нам списка.
                                            # Далее по коду, с остальными двумя таблицами буду работать по id водителя.
                    out_list.append(temp_list_route) # сохраняем список в новый.
                elif out_list == [] and count >= route_list_len: # условие - при отсутствии во восходящих данных
                                            # необходимого нам маршрута,то вернемся на шаг назад, для повторного ввода маршрута.
                    input('Такого маршрута нет\nНажмите ENTER для для повтора ввода >>>:')
                    return # шаг назад.

            bus_list = fn.reading_from_file('bus.txt') # получение данных из таблицы bus.txt .
            for i in range(len(bus_list)): # проходим по каждому вложению в список.
                temp_list_bus = []
                for j in bus_list[i]: # заглядываем в каждый вложенный список списков.
                    temp_list_bus.append(j)
                if temp_list_bus[0] == id: # если id водителя, из водящих данных (а это таблица и ее столбцы не изменяемы,
                                            # предположим) совпадает, с найденным ранее (первая часть кода)
                                            # id водителя через поиск маршрута, то ..
                    out_list.append(temp_list_bus) # найденный список добавляем к найденному ранее, в конец списка.

            driver_list = fn.reading_from_file('driver.txt') # получение данных из таблицы driver.txt
            for i in range(len(driver_list)):
                temp_list_driver = []
                for j in driver_list[i]:
                    temp_list_driver.append(j)
                if temp_list_driver[0] == id: # аналогично, находим нужный id.
                    out_list.append(temp_list_driver) # и добавляем в конец.
                    unique_list = reduce(lambda x,y: x+y,out_list) # Убираем вложенные списки, сейчас все данные в одном списке.
                        # reduce - это функция из встроенного модуля functools -> УМЕНЬШАТЬ.
                    list_print = []
                    [list_print.append(item) for item in unique_list if item not in list_print] # Создаем уникальность списка,
                                                                                                # удаляем повторы данных.
                    print_driver_file(list_print)# печать в консоль.



def search_id_data(): # поиск по id водителя.
    while True:
            cl.clear_screen()
            route_list = fn.reading_from_file('route.txt') # получение данных из таблицы route.txt
            route_list_len = len(route_list) # узнал количество вложений в списке.
            out_list = []
            count = 0
            id = input('Нажмите ENTER для возврата в меню,\nИЛИ введите id водителя ->:')
            if id == '':
                return # выводит для повтора ввода id.
            for i in range(len(route_list)):
                count +=1 # считаю количество проходов, списков в списке.
                temp_list_route = []
                for j in route_list[i]:
                    temp_list_route.append(j) # раскрываю внутренние списки, каждое вложение в начальном списке.
                if temp_list_route[0] == id: # если на позиции id из входящих данных совпадает с введенным, то строка 57.
                    out_list.append(temp_list_route) # сохраняем список в новый.
                elif out_list == [] and count >= route_list_len: # условие - при отсутствии во восходящих данных
                                            # необходимого нам id,то вернемся на шаг назад, для повторного ввода id.
                    input('Такого id нет\nНажмите ENTER для для повтора ввода >>>:')
                    return # шаг назад.

            bus_list = fn.reading_from_file('bus.txt') # получение данных из таблицы bus.txt .
            for i in range(len(bus_list)): # проходим по каждому вложению в список.
                temp_list_bus = []
                for j in bus_list[i]: # заглядываем в каждый вложенный список списков.
                    temp_list_bus.append(j)
                if temp_list_bus[0] == id: # если id водителя, из водящих данных (а это таблица и ее столбцы не изменяемы, предположим)
                                            # совпадает с введенным id водителя, то ...
                    out_list.append(temp_list_bus) # найденный список добавляем к найденному ранее, в конец списка.

            driver_list = fn.reading_from_file('driver.txt') # получение данных из таблицы driver.txt
            for i in range(len(driver_list)):
                temp_list_driver = []
                for j in driver_list[i]:
                    temp_list_driver.append(j)
                if temp_list_driver[0] == id: # аналогично, находим нужный id.
                    out_list.append(temp_list_driver) # и добавляем в конец.
                    unique_list = reduce(lambda x,y: x+y,out_list) # Убираем вложенные списки, сейчас все данные в одном списке.
                        # reduce - это функция из встроенного модуля functools -> УМЕНЬШАТЬ.
                    list_print = []
                    [list_print.append(item) for item in unique_list if item not in list_print] # Создаем уникальность списка,
                                                                                                # удаляем повторы данных.
                    print_driver_file(list_print) # печать в консоль.


def print_driver_file(data):  # Форматирование данных поиска на печать. Таблица.
    cl.clear_screen()
    print('|id|\t   Фамилия |\t       Имя |\t    Отчество | № марш.|\t                    '\
                    'маршрут автобуса |\tгос номер |    модель |  состояние | стаж вождения |')
    print('-'*156)
    print("|{0:>2}| {1:>13} | {2:>13} |{3:>16} |{4:>7} | {5:>36} |{6:>11} |{7:>10} |{8:>11} |{9:>14} |"\
            .format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
    print()
    input('Нажмите ENTER для возврата в меню >>>:')

