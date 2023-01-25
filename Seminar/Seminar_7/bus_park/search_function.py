import clear as cl
import time



def second_menu():
    while True:
        cl.clear_screen()
        print('Автопарк\n')
        print('Список команд:')
        ch = input('1 - Поиск по фамилии\n2 - Поиск по id\n3 - Поиск по маршруту\n'\
                    '4 - Возврат в основное меню\n\nВведите номер команды ->: ')
        if ch == '1':
            input()
        if ch == '2':
            input()
        if ch == '3':
            input()
        if ch == '4':
            print('Куда же Вы...')
            time.sleep(1)
            return

