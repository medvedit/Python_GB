# Задача №1 ______________________________________________________________
# Задайте строку из набора чисел. Напишите программу, которая покажет наибольшее и наименьшее число.
# В качестве разделителя используйте пробел.

list_str = '1, 4, 34. 554: -56; 0, 58" -2, 49'

def user_input(user_srt: str) -> list:
    new_str = user_srt.split()
    list_out = []

    for i in range(len(new_str)):
        new_str[i] = new_str[i].strip(',.:"`~_!?')
        if new_str[i].replace('-', '', 1).isdigit():
            list_out.append(new_str[i])
    return list_out

def user_output(list_sort):
    if list_sort:
        return min(list_sort, key=int), max(list_sort, key=int) # Всторенный метод сортировки min или max -> метод(где, что бы воспринимал цифры в строке как единое целое)
    return 'Получен не список цифр...'


print(f'Строка зашла в первую функцию -> {list_str}')
ls = (user_input(list_str))
print(f'Убрали лишние разделители. Строка на выходе из первой функции -> {ls}')
min_max = user_output(ls)
print(f'Min end Max -> {min_max}')

# Задача №2 ______________________________________________________________
# Найдите корни квадратного уравнения Ax**2 + Bx + C = 0, С помощью модуля. Запросите значения A, B, C 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

def discriminant(a, b, c):
    D = b**2-4*a*c
    print(D)
    with open('/Users/Medwed_SA/Desktop/Education/Python/Знакомство с языком Python/Lecture_end_Seminare/'\
                'Python_GB/Seminar/2_Sem_4_task2_file.txt', 'a', encoding="utf-8") as my_file:
        my_file.write(F'{a}x**2 + {b}x + {c} = 0\n')
        if D > 0:
            x_1 = (-b+sqrt(D))/(2*a)
            x_2 = (-b-sqrt(D))/(2*a)
            # my_file.write(f'Первый корень -> {x_1}\nВторой корень -> {x_2}\n')
            print(f'Первый корень -> {x_1:.2f}\nВторой корень -> {x_2:.2f}', file=my_file)
        elif D == 0:
            # x = -b/(2*a)
            my_file.write(f'Один корень -> {-b/(2*a):.2f}\n')
        else:
            my_file.write('Нет корней...\n')

discriminant(3, 12, -12)

# Задача №3 ______________________________________________________________
# На вход программе подается число N. Программа печатает числа в треугольник. Используем вложенные циклы.

x = int(input('Введите число: '))
for i in range(1, x + 1):
    for j in range(i):
        print(i, end='')
    print()

# ____________________________________________________________________________________ HOMEWORK ____________________________________________________________________

# Задача №1: --------------------------------------------------------------------------------------------------------------
# # Вычислить число с заданной точностью d.

# Вариант 1 ___________________________________________

from decimal import Decimal

number = Decimal(input('Введите число вещественное число: '))
precision_number = Decimal(input('Введите точность вывода вещественного числа: '))

number_out = number.quantize(Decimal(precision_number))

print(number_out)
# Ответ: Введите число: 1234.92349234324
#        Введите точность: 4949399595.234
#        1234.923

# Вариант 2 ___________________________________________

num = float(input('Введите число вещественное число: '))

_, accuracy = input('Введите точность вывода введенного ранее вещественного числа числа: ').split(".") #Введенное число через сплит, через разделитель
#                                                                                  записываем левую часть в безымянную переменную _,
#                                                                                 а левую в переменную accuracy.
print(f'{num:.{len(accuracy)}f}') # по длине accuracy делаем вывод переменной num



# Задача №2: --------------------------------------------------------------------------------------------------------------
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 99876700

def prime_factors_number(n:int) -> list:
    out = []
    for i in range(2, n + 1):
        while not n % i:
            n //= i
            out.append(i)
            if n == 1:
                break
    return out

print(n) # 99800
print(prime_factors_number(n)) # [2, 2, 2, 5, 5, 499]

# Задача №3: --------------------------------------------------------------------------------------------------------------
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов последовательности, в том же порядке.

#  Вариант 1 : НО COUNT СЪЕДАЕТ МНОГО РЕСУРСОВ!!!___________________
from random import uniform

def random_list(count):
    while count < 0 or count <= 1:
        return 'Вы хотите разобрать стоку? Пожалуйста...'
    rnd_list = [(int(uniform(1, count))) for i in range(count)]
    return rnd_list


def non_repeating(val_ls):
    result = []
    for i in range(len(val_ls)):
        if val_ls.count(val_ls[i]) == 1:
            result.append(val_ls[i])
    return result

list_out = random_list(int(input('Введите число, количество элементов в списке:')))
print(list_out)
print(f'Эти элементы в встречаются один раз -> {non_repeating(list_out)}')

# Вариант 2: _________________________________________

from random import uniform

def random_list(count: int) -> list:
    while count < 0 or count <= 1:
        return 'Вы хотите разобрать стоку? Пожалуйста...'
    rnd_list = [(int(uniform(1, count))) for i in range(count)]
    return rnd_list

def search_repetition(n_list: list) -> list:
    result = []
    my_dict = {}.fromkeys(n_list, 0) # из входящего списка формируем словарь  с ключами
    print(my_dict)

    for i in n_list:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] ==1:
            result.append(k)

    return result

list_out = random_list(int(input('Введите число, количество элементов в списке:')))
print(list_out)
print(f'Эти элементы в встречаются один раз -> {search_repetition(list_out)}')

# Вариант 3: _________________________________________

from collections import Counter

first_list = [1, 2, 2, 5, 45, 6, 3, 1, 8, 6, 9, 65, 8, 4, 9, 7, 54, 0]
second_list = Counter(first_list)

result = [x for x, n in second_list.items() if n == 1]

print(result)# [5, 45, 3, 65, 4, 7, 54, 0]



# *Задача №4: ---------------------------------------------------------------------------------------------
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее трех раз.


from random import randint

k = int(input('Введите натуральную степень k:'))


def polynomial_coefficient(degree_in: int):
    max_val=10
    # коэфф. при старшей степени не должен быть равен 0
    degree_in=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
    poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(degree_in) if j][::-1])
    # Поиск и замены:
    poly=poly.replace('x^1+', 'x+')
    poly=poly.replace('x^0', '')
    poly+=('','1')[poly[-1]=='+']
    poly=(poly, poly[:-2])[poly[-2:]=='^1']
    # with open('/Users/Medwed_SA/Desktop/Education/Python/Знакомство с языком Python/'\
    #             'Lecture_end_Seminare/Python_GB/Seminar/3_poly_Sem_4_task_4.txt', 'a', encoding="utf-8") as my_file:
    #     my_file.write(F'{poly}\n')
    # with open('/Users/Medwed_SA/Desktop/Education/Python/Знакомство с языком Python/Lecture_end_Seminare/'\
    #             'Python_GB/Seminar/3.1_poly_Sem_4_task_4.txt', 'a', encoding="utf-8") as my_file:
    #     my_file.write(F'{poly}\n')
    return poly

print(polynomial_coefficient(k))


# **Задача №5: --------------------------------------------------------------------------------------------------------------
# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.

def polynomial_sum(name_1:str, name_2:str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readline()
        second = my_f_2.readline()

        if len(first) == len(second):
            with open('/Users/Medwed_SA/Desktop/Education/Python/Знакомство с языком Python/'\
                        'Lecture_end_Seminare/Python_GB/Seminar/4_poly_Sem_4_task_5.txt','a', encoding="utf-8") as my_f_3:
                for i, v in enumerate(first):
                    my_f_3.write(f'{v[:-5]} + {second[i]}')
        else:
            print('Содержимое файлов не совпадает.')

polynomial_sum('3_poly_Sem_4_task_4.txt', '3.1_poly_Sem_4_task_4.txt')





