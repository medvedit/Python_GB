# Задача 25: ------------------------------------
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

import os
import re
string_abc = 'a a a b c A a d c D d'


def Number_Characters_String(word):  # Метод подсчета симолов в строке
    res = ''  # Создали строкавую переменную
    data = {}  # Создали пустой словарь
    array = word.lower().split()  # разделили строку на список подстрок по разделителю
    print(array)
    for i in array:  # идем по всем символам
        if i in data:  # если символ есть в в словаре data, то выполняется строка ниже, иначе переходим else
            data[i] += 1 # к символу (в данный момент это ключь в словаре) добавляем значение (порядковый номер)
            res += i + '_' + str(data[i]) + ' ' # в строковый результат записываем символ + разделитель + str порядковый номер + пробел
        else:
            data[i] = 0 # к символу (в данный момент это ключь в словаре) добавляем значение (порядковый номер)
            res += i + ' '  # в строковый результат записываем символ + пробел
    return res


print(Number_Characters_String(string_abc))

# Задача №27 ------------------------------------------------------------
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

os.system('clear')

string = 'She sells sea shells on the sea shore The shells that she sells are sea shells I\'m sure.So if she sells sea shells on the sea shore I\'m sure that the shells are sea shore shells'
print(string)
print()

string = string.replace('.', " ") # что бы убрать точку и сделать пробел мажду двумя словами ( sure.So )


def Number_of_Words_Text(string_in):  # Удаляем все символы из строки, не создовая доплнительных пробелов.
    string_out = re.sub(r'[!,."\']', '', string_in)
    word_amount = {}
    count_word = 0
    count_unique_word = 0
    string_test = string_out.lower().split() # print(string_out) # можно проверить
    print()
    print('Каждое слово + количество раз встретилось в тексте.')

    for i in string_test:
        if i in word_amount:
            word_amount[i] += 1
        else:
            word_amount[i] = 1

    for item in word_amount:  # for (k,v) in dictionary.items():
        print(f'{item} = {word_amount[item]}') # print('{}: {}'.format(item, dictionary[item]))
    print()

    for item in word_amount:
        count_word += word_amount[item]
    print(f'Общее количество слов в тексте = {count_word}')

    for item in word_amount:
        count_unique_word += 1
    print(f'Количество различных слов в тексте = {count_unique_word}')
    print()


Number_of_Words_Text(string)


# Задача №29 ------------------------------------------------
# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# Прервый ариант Вани ЛУЧШИЙ !!! стр 89 исправил 1000 на n , и стр 92 сменил знак с > на < И ВСЁ!
n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

# Вариант "свой"(от ученика, игнорирующего переподавателя..)
n = int(input('введи число N:'))
if n != 0:
    max_number = n
while n != 0:
    if max_number < n:
        max_number = n
        n = int(input('введи следуещее число N:'))
        print('максимальное число {}'.format(max_number))
    else:
        print('чисел нет')


# ========================================================================================================= Домашняя работа ===========================================================

# Задача 22: ---------------------------------------------------------
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

os.system('clear')

length_set1 = int(input('Введите длину набора №1: '))
length_set2 = int(input('Введите длину набора №2: '))
num_min = -19
num_max = 50


def Number_Arrey(x, min, max):  # заполнение рандом
    import random
    m = []
    for i in range(0, x):
        random_number = round(random.randint(min, max))
        m.append(random_number)
    return m


first_set = set(Number_Arrey(length_set1, num_min, num_max)) # преобразуем в множество
second_set = set(Number_Arrey(length_set2, num_min, num_max))  # преобразуем в множество
print(first_set)
print(second_set)
print()
common_intersection = first_set.intersection(second_set)  # находим пересечение данных

# end_set = sorted(common_intersection) # сортировка множества для вывода с помощью sorted
# print(end_set)

final_list = list(common_intersection)


def Sort_Increase(number_list):  # метод сортировки чисел по возрастанию
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            if number_list[i] > number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
    return number_list


print(Sort_Increase(final_list))


# Задача 24: -----------------------------------------------------
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# Значения сгенерированы случайным образом
# 4 2 3 1
# Output: 9

os.system('clear')

shrub_amount = int(input('Введите клоичество кустов на грядке: '))
num_min = 1
num_max = 956


def Number_Arrey(x, min, max):  # заполнение рандом
    import random
    m = []
    for i in range(0, x):
        random_number = round(random.randint(min, max))
        m.append(random_number)
    return m


shrub_lenght = Number_Arrey(shrub_amount, num_min, num_max)

print(shrub_lenght)
print()


def Maximum_Sum_Three(number_list):
    sum_max = 0
    for i in range(len(shrub_lenght)-1):
        if sum_max < shrub_lenght[i] + shrub_lenght[i-1] + shrub_lenght[i+1]:
            sum_max = shrub_lenght[i] + shrub_lenght[i-1] + shrub_lenght[i+1]
        if shrub_lenght[0] + shrub_lenght[-1] + shrub_lenght[-2] > sum_max:
            sum_max = shrub_lenght[0] + shrub_lenght[-1] + shrub_lenght[-2]
    return sum_max


print(Maximum_Sum_Three(shrub_lenght))