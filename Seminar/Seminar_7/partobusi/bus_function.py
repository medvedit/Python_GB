import clear as cl
import main_function as fn
import time


def bus_print_file(data_file):  # Форматирование данных на печать. Таблица.
    cl.clear_screen()
    output_data = fn.reading_from_file(data_file)
    print('| № | id автобуса |\tгос. номер  |\t  модель     |\t состояние  |\t№ маршрута |')
    print('-'*84)
    for num_str,bus in enumerate(output_data):
        num_str = num_str+1
        print("| {0:^1} | {1:>11} | {2:>15} |{3:>15} |{4:>13} |{5:>13} |"\
                .format(num_str, bus[0], bus[1], bus[2], bus[3], bus[4]))
    print()
    input('Нажмите ENTER для возврата в меню >>>')



def bus_add(data): # Добавление данных в bus.txt
    cl.clear_screen()
    while True:
        print('Добавление данных: ')
        buses_list = fn.reading_from_file(data)
        new_bus_list = []
        print(fn.print_bus())
        print()
        print('Сейчас Вам предложат ввести данные\n'\
                'Таблицу с образцом ввода данных Вы видите выше\n'\
                '>>> Для выхода нажмите Enter <<<\n')
        id_bus = str(input('id автобуса ->:  '))
        if id_bus == "":
            return
        new_bus_list.append(id_bus)
        new_bus_list.append(str(input('гос. номер ->:  ').upper()))
        new_bus_list.append(str(input('модель ->: ')))
        new_bus_list.append(str(input('состояние ->: ').lower()))
        new_bus_list.append(str(input('№ маршрута ->: ')))
        if "" in new_bus_list:
            return
        buses_list.append(new_bus_list)
        print('Автобус добавлен!')
        time.sleep(2)
        fn.save_data_to_file(data, buses_list)


