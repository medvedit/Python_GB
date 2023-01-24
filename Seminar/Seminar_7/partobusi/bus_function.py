import clear as cl
import function as fn



def bus_printing(data_file):  # Форматирование данных на печать. Таблица.
    cl.clear_screen()
    output_data = fn.reading_from_file(data_file)
    print('| id автобуса |\tгос. номер  |\t  модель     |\t состояние  |\t№ маршрута |')
    print('-'*76)
    for id,bus in enumerate(output_data):
        id = id+1
        print("| {0:^11} | {1:>11} | {2:>14} |{3:>13} |{4:>13} |"\
                .format(id, bus[0], bus[1], bus[2], bus[3]))
    print()
    input('Нажмите ENTER для возврата в меню >>>')

    