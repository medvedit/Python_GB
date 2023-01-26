import clear as cl
import time
import main_txt_function as fn
import sys
from functools import reduce



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
    search_surname_data('route.txt')

def search_id():
    search_id_data('route.txt')

def route_number_search():
    route_number_search_data()


# def route_number_search_data():
#     while True:
#         cl.clear_screen()
#         route_list = fn.reading_from_file('route.txt')
#         print(route_list)
#         input()
#         out_list = []
#         route = input('Нажмите ENTER для возврата в меню\nили введите номер маршрута ->:')
#         if route == '':
#             return
#         for i in range(len(route_list)):
#             temp_list_route = []
#             for j in route_list[i]:
#                 temp_list_route.append(j)
#             if temp_list_route[4] != route:
#                 print('Такого маршрута нет')
#                 return
#             elif temp_list_route[4] == route:
#                 id = temp_list_route[0]
#                 out_list.append(temp_list_route)
#                 return id, out_list

def route_number_search_data():
    while True:
            # cl.clear_screen()
            route_list = fn.reading_from_file('route.txt')
            # print(route_list)
            # input()
            route_list1 = len(route_list)
            out_list = []
            cou = 0
            route = input('Нажмите ENTER для возврата в меню\nили введите номер маршрута ->:')
            # if route == '':
            #     return
            for i in range(len(route_list)):
                cou +=1
                temp_list_route = []
                for j in route_list[i]:
                    # cou += 1
                    temp_list_route.append(j)
                if temp_list_route[4] == route:
                    id = temp_list_route[0]
                    out_list.append(temp_list_route)
                    # return id, out_list
                elif out_list == [] and cou >= route_list1:
                    input('Такого маршрута нет')
                    # time.sleep(1)
                    return

            bus_list = fn.reading_from_file('bus.txt')
            for i in range(len(bus_list)):
                temp_list_bus = []
                for j in bus_list[i]:
                    temp_list_bus.append(j)
                if temp_list_bus[0] == id:
                    out_list.append(temp_list_bus)

            driver_list = fn.reading_from_file('driver.txt')
            for i in range(len(driver_list)):
                temp_list_driver = []
                for j in driver_list[i]:
                    temp_list_driver.append(j)
                if temp_list_driver[0] == id:
                    out_list.append(temp_list_driver)
                    e = reduce(lambda x,y: x+y,out_list)
                    new_list = []
                    [new_list.append(item) for item in e if item not in new_list]
                    print_driver_file(new_list)





def print_driver_file(data):  # Форматирование данных на печать. Таблица.
    cl.clear_screen()
    # output_data = fn.reading_from_file(data_file)
    print('| id водителя |\tФамилия    |\t     Имя    |\t Отчество     |\t№ маршрута |\t маршрут автобуса |\tгос номер |\tмодель |\tсостояние |\tстаж вождения |')
    print('-'*87)
    # print(data)
    # input()
    # for num_str,data in enumerate(data_file):
    #     num_str = num_str+1
    print("| {0:^1} | {1:>11} | {2:>14} |{3:>15} |{4:>16} |{6:>14} |{7:>14} |{8:>14} |{9:>14} |"\
            .format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
    print()
    input('Нажмите ENTER для возврата в меню >>>')