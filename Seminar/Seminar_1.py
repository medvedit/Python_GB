#12.12.2022 # Грохаем алгоритмы Адитья
# За день машина проезжает n километров. Сколько суток нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: # n = 700       # Output:  2
#          m = 750
n = 700
m = 750
def distance(a, x):
    t = (a + x - 1) // a
    return t
print(distance(n,m))


# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
a = int(input('Первый класс =>'))
b = int(input('Первый класс =>'))
c = int(input('Первый класс =>'))
sum = a % 2 + b % 2 + c % 2 + (a // 2 + b // 2 + c // 2)
print(sum)


# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

i = int(input("порядковый номер вагона: "))
j = int(input("номер на вагоне: "))
if i - j == 0:
    c = 0
else:
    c = i + j - 1
print(c)

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним,
# что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.
# Input: 2016
# Output: YES

year = int(input('Введите год: '))
if (year % 4 == 0 and not year % 100) or (year % 400 == 0):
    print("yes")
else:
    print("no")

# ---------------------------------------------------------------------------------------------- ДОМАШНЯЯ РАБОТА ---------------------------------------------------------------------------------------------------

# Задача 2 ===========================================================================================
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# ПЕРВОЕ РЕШЕНИЕ +++++
import random
number_of_segments_length = random.randint(100, 999)
seсond_namber = number_of_segments_length
sum_digits = 0
while seсond_namber != 0:
    sum_digits += (seсond_namber % 10)
    seсond_namber //= 10
else:
    print('Пожалуй')
    print('Хватит))')
print(F'{number_of_segments_length} -> {sum_digits} ({number_of_segments_length // 100} \
+ {number_of_segments_length % 100 // 10} + {number_of_segments_length % 10})')


# ВТОРОЕ РЕШЕНИЕ +++++
import random
num = random.randint(100, 999)
sun_num = 0

def Digits_Sum(first_number, second_number):
    while first_number != 0:
        second_number += (first_number % 10)
        first_number //= 10
    return second_number

print(f'{num} -> {Digits_Sum(num, sun_num)}')


# ТРЕТЬЕ РЕШЕНИЕ +++++
def Get_Number():
    while True:
        get_number = input(
            'Введите целое, положительное, трехзначенное число число: ')
        if get_number.isdigit() and len(get_number) == 3:
            return get_number

sum_number = int(Get_Number())

def Digits_Sum(first_number):
    second_number = 0
    while first_number != 0:
        second_number += (first_number % 10)
        first_number //= 10
    return second_number

print(f'{sum_number} -> {Digits_Sum(sum_number)} ({sum_number // 100} \
+ {sum_number % 100 // 10} + {sum_number % 10})')


# Задача 4 ==========================================================================================
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример: 6 -> 1 4 1
#         24 -> 4 16 4
#         60 -> 10 40 10


# ПЕРВОЕ РЕШЕНИЕ +++++
print('Введите колличество журавликов: ')
s = int(input())
if s % 6 or s < 6:
    print('Введите число кратное 6')
else:
    print(f'{s} -> {s//6} {s//6*4} {s//6}')


# ВТОРОЕ РЕШЕНИЕ +++++
print('Введите колличество журавликов: ')
a = int(input())

def Number_of_Birds(x):
    if x % 6 or x < 6:
        return print('Введите число кратное 6')
    else:
        return print(f'{x} -> {x//6} {x//6*4} {x//6}')

Number_of_Birds(a) # в ответе + появляется строка None - не понимаю что это..


# Задача 6 =============================================================================================
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# ПЕРВОЕ РЕШЕНИЕ +++++
from random import randint
number_of_segments_length = [randint(0,9) for x in range(6)]
n1 = number_of_segments_length[0]+number_of_segments_length[1]+number_of_segments_length[2]
n2 = number_of_segments_length[3]+number_of_segments_length[4]+number_of_segments_length[5]
if n1 == n2:
    print(f'{number_of_segments_length} {n1} = {n2} -> yes')
else:
    print(f'{number_of_segments_length} {n1} ≠ {n2} -> no')

# [6, 2, 0, 1, 2, 5] 8 = 8 -> yes
# [2, 0, 5, 4, 9, 4] 7 ≠ 17 -> no

# ВТОРОЕ РЕШЕНИЕ +++++
number_of_segments_length = 385916
if (number_of_segments_length // 100000) + (number_of_segments_length // 10000 % 10)\
    +(number_of_segments_length // 1000 % 10) == (number_of_segments_length // 100 % 10)\
    + (number_of_segments_length // 10 % 10) + (number_of_segments_length %10):
    print(f'{number_of_segments_length} -> yes')
else:
    print(f'{number_of_segments_length} -> no')

# 385916 -> yes
# 123456 -> no

# Задача 8 ==========================================================================================
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек в длину: ')) # n = number_of_segments_length
m = int(input('Введите количество долек в ширину: ')) # m = number_of_segments_width
k = int(input('Сколько долек вы хотите отломить за один разлом: ')) # k = break_off_segments

if n * m < k:
    print(f'{n} {m} {k} -> no')
elif m * n == k:
    print(f'Можно не ломать, вся шоколадка Ваша)))')
elif k % m == 0 or k % n == 0:
    print(f'{n} {m} {k} -> yes')
else:
    print(f'{n} {m} {k} -> no')

