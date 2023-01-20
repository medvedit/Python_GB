from datetime import datetime as dt
from time import time


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/Medwed_SA/Desktop/Education/Python/'\
            'Знакомство с языком Python/Lecture_end_Seminare/'\
            'Python_GB/Lecture/Lecture_4/join_job/log.cvs', 'a') as file:
        file.write('{};temperature -> {}\n'
                   .format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/Medwed_SA/Desktop/Education/Python/'\
            'Знакомство с языком Python/Lecture_end_Seminare/'\
            'Python_GB/Lecture/Lecture_4/join_job/log.cvs', 'a') as file:
        file.write('{};pressure -> {}\n'
                   .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/Medwed_SA/Desktop/Education/Python/'\
            'Знакомство с языком Python/Lecture_end_Seminare/'\
            'Python_GB/Lecture/Lecture_4/join_job/log.cvs', 'a') as file:
        file.write('{};wind_speed -> {}\n'
                   .format(time, data))
