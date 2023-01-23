import time
from print_function import print_data
from search_function import search_in_file
from print_function import output_data_string

count_str = print_data()


def del_data():  # Меню удаления.
    while True:
        clear_screen()
        print('Выберите пункт меню:')
        print("1 - удаление по номеру записи\n"
              "2 - удаление по поиску\n"
              "3 - выход")
        reply = input("->:").upper()
        match reply:
            case "1":
                del_data_by_number()
            case "2":
                del_data_by_search()
            case "3":
                return
            case _:
                print("неверный ввод")
                time.sleep(1)



def del_data_by_number():# Удаление по номеру записи.
    while True:
        clear_screen()# Очистили консоль.
        print_data()# Распечатали телефонную книгу с нумерацией каждой записи.
        print()
        reply = input(">>> Введите цифру 0 для выхода <<<\nВведите номер записи для удаления ->:")
        if reply.upper() == "0":
            return
        elif not reply.isnumeric():# Проверка на ввод числа.
            print('Не корректный ввод\n'\
                    'Нужно ввести номер строки >>>')
            time.sleep(2) # Задержка 3сек. для вывода текста, затем приглашение к повторному вводу.
            continue
        number = int(reply) # Присвоение к int из str.
        if number > count_str:# Сверяем с количеством строк записей из global переменной в методе print_function.py/print_data()
            print('Записи с таким номером не существует >>>')
            time.sleep(2)
            continue
        if number <= count_str: # Сверяем с количеством строк записей из global переменной в методе print_function.py/print_data()
            print(f'Вы желаете удалить запись под номером {number}?')
            if input('Удаление -> цифра 1 -> ДА // >>> Enter <<< -> НЕТ ->:').upper() == "1": # Уточнение удаления.
                phone_data = ""
                count = 0
                with open('phone_book.txt', "r", encoding="utf8") as datafile:
                    for line in datafile:
                        count += 1
                        if number == count: # Если удаляемая строка == count,
                            continue # то пропускаем.
                        phone_data += line # Иначе записываем строку.
                with open('phone_book.txt', "w", encoding="utf8") as datafile:
                    datafile.write(phone_data) # Перезаписываем телефонную книгу.


def del_data_by_search():  # Удаление записи через поиск.
    while True:
        clear_screen()
        reply = input(">>> Enter - выход <<<\nСтрока поиска по фамилии для удаления записи ->: ").capitalize() # первая буква заглавная.
        if reply == "":
            return
        found_records = search_in_file(reply)
        if len(found_records) == 0:
            print("Нет записей для удаления")
            time.sleep(2)
        else:
            print("Найдены записи:")
            for print_data in found_records:
                output_data_string(print_data)
            print()
            if input('Удаляем все найденные записи?\n'\
                    'Иначе введите фамилию полностью\n'\
                    'Цифра 1 -> ДА // >>> Enter <<< -> НЕТ ->:').upper() == "1":
                phone_data = ""
                with open("phone_book.txt", "r", encoding="utf8") as data_file:
                    for line in data_file:
                        if reply in line:
                            continue
                        phone_data += line
                with open("phone_book.txt", "w", encoding="utf8") as data_file:
                    data_file.write(phone_data)


from main import clear_screen