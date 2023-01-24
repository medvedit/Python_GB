import bus_function as bus

def reading_from_file(data):  # Чтение из файла .txt
    print()
    with open(data, "r", encoding="utf8") as datafile:
        result = []
        for line in datafile:
            line = line.replace('\n', '')
            result.append(line.split(','))
        return result



def save_data_to_file(name, data_list): # Сохранение в файл .txt
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')



def print_bus():
    return bus.bus_printing('bus.txt')

def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))

def print_driver():
    return list_numbering('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))

def print_route():
    return list_numbering('route.txt')

def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))




