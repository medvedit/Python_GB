from print_function import print_data
import time

number_global = 0
count_str = print_data()



def line_search_editor():
    global number_global
    while True:
        clear_screen()
        print_data()# Распечатали телефонную книгу с нумерацией каждой записи.
        print()
        reply = input("Введите цифру 0 для перехода в основное меню\nили\n"\
                        "Введите номер записи для редактирования ->:")
        if reply.upper() == "0":
            return
        elif not reply.isnumeric():# Проверка на ввод числа.
            print('Не корректный ввод\n'\
                    'Нужно ввести номер строки >>>')
            time.sleep(3) # Задержка 3сек. для вывода текста, затем приглашение к повторному вводу.
            continue
        number = int(reply) # Присвоение к int из str.
        if number > count_str:
            print()
            print('Записи с таким номером не существует >>>')
            time.sleep(3)
            continue
        if number <= count_str: # Сверяем с количеством строк записей.
            print()
            print(f'Вы желаете начать редактирование записи под номером {number}?')
            if input('Цифра 1 -> Да // Любая другая клавиша -> Нет ->:').upper() == "1": # Уточнение удаления.
                number_global = number
                change_menu()



def change_menu():
    while True:
        clear_screen()
        print('Выберете пункт для редактирования')
        print("1 - Фамилия\n"
              "2 - Имя\n"
              "3 - Отчество\n"
              "4 - Номер телефона\n"
              "5 - Вернуться назад")
        reply = input("->:").upper()
        match reply:
            case "1":
                data_index = 0
                editor_data(data_index)
            case "2":
                data_index = 1
                editor_data(data_index)
            case "3":
                data_index = 2
                editor_data(data_index)
            case "4":
                data_index = 3
                editor_data(data_index)
            case "5":
                return
            case _:
                print("Неверный ввод\n"\
                    "Нужно выбрать цифру пункта меню")
                time.sleep(2)


def editor_data(index):
    if index == 3:
        phone_data = ""
        count = 0
        with open('phone_book.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if number_global == count: # Если удаляемая строка == count,
                    line_1 = line.split(',')
                    del line_1[3]
                    line_1.append(input('Введите новые данные ->:')+'\n')
                    line = ','.join(line_1)
                phone_data += line # Иначе записываем строку.
        with open('phone_book.txt', "w", encoding="utf8") as datafile:
            datafile.write(phone_data) # Перезаписываем телефонную книгу.
    else:
        phone_data = ""
        count = 0
        with open('phone_book.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if number_global == count: # Если удаляемая строка == count,
                    line_1 = line.split(',')
                    line_1[index] = input('Введите новые данные ->:').capitalize()
                    line = ','.join(line_1)
                phone_data += line # Иначе записываем строку.
        with open('phone_book.txt', "w", encoding="utf8") as datafile:
            datafile.write(phone_data) # Перезаписываем телефонную книгу.



from clear import clear_screen
