from menu import Menu
import function as fn

# if __name__ == "__main__":
#     # основной блок
menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Вывод водителей"),
        ("4", "Добавление водителей"),
        ("5", "Вывод маршрута"),
        ("6", "Добавление маршрута"),
        ("7", "Выход", lambda: exit())]

menu = Menu(menuitems)
    # menu.run('>:')

for i in menuitems:
    print(i[0],i[1])

text = input("Введите номер: ")
if text == '1':
    print(fn.print_bus())
elif text == '2':
    fn.add_bus()
elif text == '3':
    print(fn.print_driver())
elif text == '4':
    fn.add_driver()
elif text == '5':
    print(fn.print_route())
elif text == '6':
    fn.add_route()
elif text == '7':
    exit()
