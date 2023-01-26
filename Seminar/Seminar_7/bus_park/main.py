import main_txt_function as fn
import clear as cl
import time
import search_function as sf



if __name__ == "__main__":   # основное меню
    menu = (f"Автопарк\n\n"
            "Список команд:\n"
            "1 - Вывод автобусов\n"
            "2 - Добавление автобуса\n"
            "3 - Вывод водителей\n"
            "4 - Добавление водителей\n"
            "5 - Вывод маршрута\n"
            "6 - Добавление маршрута\n"
            "7 - Поиск по данным\n"
            "8 - Выход\n")
    while True:
        cl.clear_screen()
        print(menu)
        answer = input("Введите номер команды ->:").upper()
        match answer:
            case "1":# Печать автобусов
                print(fn.print_bus())
            case "2":# Добавление автобусов
                fn.add_bus()
            case "3":# Печать водителей
                print(fn.print_driver())
            case "4":# Добавление водителей
                fn.add_driver()
            case "5":# Печать маршрутов
                print(fn.print_route())
            case "6":# Добавление маршрутов
                fn.add_route()
            case "7": # Поиск по данным
                sf.second_menu()
            case "8":# выход
                cl.clear_screen()
                exit(0)
            case _:
                print("Неверный ввод. Повторите ввод: ")
                time.sleep(1) # задержка для повторного ввода в 1сек.

