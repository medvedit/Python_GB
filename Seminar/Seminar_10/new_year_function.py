import datetime
import emoji

def new_year():
    x = datetime.datetime.today().strftime("%-d.%-m.%Y.%-H.%-M.%-S")
    y = x.split('.')

    day = int(y[0])
    temp_month = int(y[1])
    temp_year = int(y[2])
    temp_hour = int(y[3])
    temp_minute = int(y[4])
    temp_second = int(y[5])


    if temp_month == 1:
        month = 0
    if temp_month == 2:
        month = 31
    if temp_month == 3:
        if temp_year // 4  and temp_year // 100 and temp_year // 400:
            month = 60
        else:
            month = 59
    if temp_month == 4:
        month = 90
    if temp_month == 5:
        month = 120
    if temp_month == 6:
        month = 151
    if temp_month == 7:
        month = 181
    if temp_month == 8:
        month = 212
    if temp_month == 9:
        month = 243
    if temp_month == 10:
        month = 273
    if temp_month == 11:
        month = 304
    if temp_month == 12:
        month = 334

    temp_result = month + day

    hour = 23 - temp_hour
    minute = 59 - temp_minute
    second = 59 - temp_second

    result = 365 - temp_result

    return f'До нового года осталось:\n{result} дней {hour} часов\n' \
            f'{minute} минут {second} секунд ' + emoji.emojize(':evergreen_tree:')



''' Этот код не активирован, но оставил тут))) Сверял итог своего кода с ниже написанным.

now = datetime.datetime.today()
NY = datetime.datetime(now.year + 1, 1, 1)
d = NY-now

mm, ss = divmod(d.seconds, 60)
hh, mm = divmod(mm, 60)

print('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))'''