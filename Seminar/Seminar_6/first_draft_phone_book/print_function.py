from clear import clear_screen



def print_all_data():  # Вывод общего количества данных.
    clear_screen()
    count = print_data()
    print()
    input("Общее количество записей {}.  Enter для выхода ->:".format(count))


def print_data():  # Вывод всех данных с нумерацией каждой строки.
    count_str = 0
    with open("phone_book.txt", "r", encoding="utf8") as datafile:
        for line in datafile:
            count_str += 1
            print(":{:<3} ".format(count_str), end='')
            output_data_string(line.strip('\n'))
        return count_str


def output_data_string(data_print:str):  # Форматирование вывода данных.
    parse_data = data_print.split(",")
    template = "{0:<33} Тел.: {1:<13}"
    print(template.format(
        parse_data[0]+' ' + parse_data[1]+' '+parse_data[2], parse_data[3]))
