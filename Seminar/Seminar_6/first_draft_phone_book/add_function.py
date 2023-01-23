from clear import clear_screen


def add_data():  # Собираем в один список новые данные.
    clear_screen()
    while True:
        print('>>> Для выхода нажмите Enter <<<\nДобавление записи:')
        last_name = input("Фамилия: ").capitalize()
        if last_name == "":
            return
        first_name = input("Имя: ").capitalize()
        patronymic = input("Отчество: ").capitalize()
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def save_data_to_file(data_to_save):  # Записываем новый список в файл .txt
    data_to_save = ",".join(data_to_save) + "\n"
    print(f'Вы добавили запись ->  {data_to_save}')
    with open("phone_book.txt", "a", encoding="utf8") as datafile:
        datafile.write(data_to_save)


