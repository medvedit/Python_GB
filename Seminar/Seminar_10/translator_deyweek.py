import datetime

dey_week = datetime.datetime.today().strftime("%A")


def change(data_in):
    data_out =''
    if data_in == 'Monday':
        data_out = 'Понедельник'
        return data_out
    elif data_in == 'Tuesday':
        data_out = 'Вторник'
        return data_out
    elif data_in == 'Wednesday':
        data_out = 'Среда'
        return data_out
    elif data_in == 'Thursday':
        data_out = 'Четверг'
        return data_out
    elif data_in == 'Friday':
        data_out = 'Пятница'
        return data_out
    elif data_in == 'Saturday':
        data_out = 'Суббота'
        return data_out
    elif data_in == 'Sunday':
        data_out = 'Воскресенье'
        return data_out

