from clear import clear_screen
from print_function import print_all_data
from add_function import add_data
from search_function import search_data
from delete_function import del_data
from editor_function import line_search_editor
import time # .sleep для приостановить выполнение программы на заданное количество секунд.


if __name__ == "__main__":   # основное меню
    menu = (f"Телефонный справочник. v.0.1\n\n"
            "Список команд:\n"
            "1 - Вывод данных\n"
            "2 - Добавление записи\n"
            "3 - Поиск\n"
            "4 - Удаление записи\n"
            "5 - Редактор данных\n"
            "6 - Выход\n")
    while True:
        clear_screen()
        print(menu)
        answer = input("Введите номер команды ->:").upper()
        match answer:
            case "1":# вывод данных
                print_all_data()
            case "2":# добавление данных
                add_data()
            case "3":# поиск
                search_data()
            case "4":# удаление данных
                del_data()
            case "5":# редактирование данных
                line_search_editor()
            case "6":# выход
                exit(0)
            case _:
                print("Неверный ввод. Повторите ввод: ")
                time.sleep(1) # задержка для повторного ввода в 1сек.
