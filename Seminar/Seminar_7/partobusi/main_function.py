import bus_function as bus
import driver_function as dvf
import route_function as rof


def reading_from_file(data):  # Чтение из файла .txt
    print()
    with open(data, "r", encoding="utf8") as datafile:
        result = []
        for line in datafile:
            line = line.replace('\n', '')
            result.append(line.split(','))
        return result



def save_data_to_file(name, data_list): # Сохранение в файл .txt
    with open(name, 'w', encoding='utf8') as datafile:
        for line in data_list:
            print(",".join(line), file=datafile)




def print_bus():
    return bus.bus_print_file('bus.txt')

def add_bus():
    bus.bus_add('bus.txt')

def print_driver():
    return dvf.print_driver_file('driver.txt')

def add_driver():
    dvf.add_driver_file('driver.txt')

def print_route():
    return rof.print_route_file('route.txt')

def add_route():
    rof.add_driver_file('route.txt')




