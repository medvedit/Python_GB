import clear as cl
import main_function as fn
import time


def print_driver_file(data_file):  # Форматирование данных на печать. Таблица.
    cl.clear_screen()
    output_data = fn.reading_from_file(data_file)
    print('| № | id водителя |\tФамилия    |\t     Имя    |\t Отчество     |\tстаж вождения |')
    print('-'*87)
    for num_str,driver in enumerate(output_data):
        num_str = num_str+1
        print("| {0:^1} | {1:>11} | {2:>14} |{3:>15} |{4:>16} |{5:>14} |"\
                .format(num_str, driver[0], driver[1], driver[2], driver[3], driver[4]))
    print()
    input('Нажмите ENTER для возврата в меню >>>')


def add_driver_file(data): # Добавление данных в driver.txt
    cl.clear_screen()
    while True:
        print('Добавление данных: ')
        driver_list = fn.reading_from_file(data)
        new_driver_list = []
        print(fn.print_driver())
        print()
        print('Сейчас Вам предложат ввести данные\n'\
                'Таблицу с образцом ввода данных Вы видите выше\n'\
                '>>> Для выхода нажмите Enter <<<\n')
        id_driver = str(input('id водителя ->:  '))
        if id_driver == "":
            return
        new_driver_list.append(id_driver)
        new_driver_list.append(str(input('Фамилия ->:  ').capitalize()))
        new_driver_list.append(str(input('Имя ->: ').capitalize()))
        new_driver_list.append(str(input('Отчество ->: ').capitalize()))
        new_driver_list.append(str(input('стаж вождения ->: ')))
        if "" in new_driver_list:
            return
        driver_list.append(new_driver_list)
        print('Водитель добавлен!')
        time.sleep(2)
        fn.save_data_to_file(data, driver_list)

