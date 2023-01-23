

def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        if len(result) > 0:
            for item in result:
                print(item[0].center(0), item[1].center(10))
        else:
            print('Таблица пустая!')

# def print_data(data):
#     if len(data) > 0:
#         print("Фамилия".center(20), "Имя".center(20),
#               "Телефон".center(15), "Примечание".center(30))
#         print("-"*85)
#         for item in data:
#             print(item[0].center(20), item[1].center(20),
#                   item[2].center(15), item[3].center(30))
#     else:
#         print("Справочник пуст!")

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')


def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))

def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))




