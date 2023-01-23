def search_data():# Приглашение к поиску.
    clear_screen()
    while True:
        reply = input(">>> Enter -> выход <<<\nНачните ввод для поиска по фамилии -> :").capitalize()
        if reply == "":
            return
        result = search_in_file(reply) # Вернули списки найденных фамилий.
        for item in result:# Проходим по всем записям.
            output_data_string(item) # Выводим каждую запись в консоль с помощью форматированного вывода функции output_data_string.
        print("Всего найдено записей: {} \n".format(len(result))) # Вывели количество найденных записей.



def search_in_file(request): # Поиск по фамилии.
    out_file = []
    with open("phone_book.txt", "r", encoding="utf8") as data_file:
        for line in data_file:
            out_file.append(line.strip("\n"))
        out_file = list(filter(lambda line: request in line[0:9], out_file)) # Поиск с 1 по 7 букву.
    return out_file



def output_data_string(data_print): # Создание форматированного вывода в консоли.
    parse_data = data_print.split(",")
    template = "{0:<33} Тел.: {1:<13}"
    print(template.format(
        parse_data[0]+' ' + parse_data[1]+' '+parse_data[2], parse_data[3]))



from main import clear_screen