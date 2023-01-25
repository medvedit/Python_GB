import time
import clear as cl
import main_txt_function as fn


def print_route_file(data_file):  # Форматирование данных на печать. Таблица.
    cl.clear_screen()
    output_data = fn.reading_from_file(data_file)
    print('| № | id водителя |\tФамилия    |\t     Имя    |\t Отчество'\
            '     |\t№ маршрута |\t         маршрут автобуса            |')
    print('-'*126)
    for num_str,route in enumerate(output_data):
        num_str = num_str+1
        print("| {0:^1} | {1:>11} | {2:>14} |{3:>15} |{4:>16} |{5:>11} | {6:>40}|"\
                .format(num_str, route[0], route[1], route[2], route[3], route[4], route[5]))
    print()
    input('Нажмите ENTER для возврата в меню >>>')


def add_driver_file(data): # Добавление данных в route.txt
    cl.clear_screen()
    while True:
        print('Добавление данных: ')
        route_list = fn.reading_from_file(data)
        new_route_list = []
        print(fn.print_route())
        print()
        print('Сейчас Вам предложат ввести данные\n'\
                'Таблицу с образцом ввода данных Вы видите выше\n'\
                '>>> Для выхода нажмите Enter <<<\n')
        id_driver = str(input('id водителя ->:  '))
        if id_driver == "":
            return
        new_route_list.append(id_driver)
        new_route_list.append(str(input('Фамилия ->:  ').capitalize()))
        new_route_list.append(str(input('Имя ->: ').capitalize()))
        new_route_list.append(str(input('Отчество ->: ').capitalize()))
        new_route_list.append(str(input('№ маршрута ->: ')))
        new_route_list.append(str(input('маршрут автобуса ->: ')))
        if "" in new_route_list:
            return
        route_list.append(new_route_list)
        print('Запись маршрута добавлена!')
        time.sleep(2)
        fn.save_data_to_file(data, route_list)

