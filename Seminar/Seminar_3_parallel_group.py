# Задача №1: ______________________________
# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, определяющую пресутствует ли в заданном списке число, полученное от пользователя.

from random import sample  # sample выдает рандомные, не повторяющиеся числа.

n = int(input('Длина списка: '))
m = int(input('какое число ищем: '))

def num_find(len_list, number):
    n_list = sample(range(1, len_list + len_list), # числа в списке от 1 до двойной длины
                    k=len_list) # сама длина списка
    print(n_list)
    if number in n_list:
        return 'yes'
    return 'no'

print(num_find(n,m))

# Задача №2: ______________________________
# Задайте список, состоящий из произвольных слов, количество задает пользователь. Напишите программу,
# которая определит индекс второго вхождения сироки в списке, либо сообщит, что его нет.

n = int(input('Введите длину: '))


def word_list(word_count, text='abc'):
    fin_list = []
    for i in range(word_count):
        temp_list = sample(text, k=3)
        fin_list.append("".join(temp_list))
    return fin_list


def find_index(wor_list, text):
    if text in wor_list and wor_list.count(text) > 1:
        index_1 = wor_list.index(text)
        print(wor_list.index(text, index_1 + 1))
    else:
        print('-1')


wr_list = word_list(n)
print(wr_list)
find_index(wr_list, input('Что ищем?: '))

# __________________________________________________________________________ Домашняя работа _______________________________________________________________________________
# Задача № 3: ______________________________
# Задайте список, состоящий из произвольных чисел, количество задает пользователь. Напишите программу,
# которая найдет сумму элементов списка, стоящих на четных позициях(не индексах).
# in                 in
# >> 4               >> 5

# out                out
# >> [7, 9, 2, 3]    >> [2, 5, 2, 7, 9]
# >> 9               >> 13

from random import sample

len_list = int(input('Введите длину списка: '))

def random_list(length_list: int) -> list:
    if len_list < 0:
        print('Введите положительное число!')
        return []

    n_list = sample(range(1, length_list + length_list), # числа в списке от 1 до двойной длины
                    k=length_list) # сама длина списка
    print(n_list)
    return n_list

out_list = random_list(len_list)

def sum_of_even_positions(rnd_list: list) -> int:
    sum_positions = 0
    for i in range(len(rnd_list)): # проход по индексам в списке.
        if not i % 2: # проверка индекса на четность. (либо,  i % 2)
            sum_positions += rnd_list[i] # складываю позицию от найденного индекса.
    return int(sum_positions)

print(sum_of_even_positions(out_list))



# Задача № 4: ______________________________
# Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# in                           in
# >> 4                         >> 5

# out                          out
# >> [8, 9, 10, 10]            >> [3, 3, 6, 8, 4]
# >> [80, 90]                  >> [12, 24, 6]

from random import sample

len_list = int(input('Введите длину списка: '))

def random_list(length_list: int) -> list:
    n_list = sample(range(1, length_list + length_list), # числа в списке от 1 до двойной длины
                    k=length_list) # сама длина списка
    print(n_list)
    return n_list

out_list = random_list(len_list)

def product_two_numbers(rnd_list: list) -> list:
    end_list = []
    len_list = len(rnd_list)
    for i in range(len_list//2):
        end_list.append(rnd_list[i] + rnd_list[len(rnd_list) - i - 1])
    if len_list % 2:
        end_list.append(rnd_list[len(rnd_list)//2])
    return end_list

print(product_two_numbers(out_list))


# Задача № 5: ______________________________
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без использования встроенной
# функции преобразования, строк.

# in          in
# >> 13       >> 88

# out         out
# >> 1101     >> 1011000

n = int(input()) # 88

def convert_to_binary(number: int) -> list:
    b = []
    while number > 0:
        b.insert(0, number % 2)
        number //= 2
    # print(*b, sep='') # решение от преподавателя
    return b

binary = convert_to_binary(n)
print(binary) # [1, 0, 1, 1, 0, 0, 0]
nam_out = ''.join(map(str,binary))
print(nam_out) # 1011000
print(type(nam_out)) #  <class 'str'>


# * Задача № 6: ______________________________
# Задайте список из произвольных вещественных чисел, количество задает пользователь. Напишите программу,
# которая найдет разницу между максимальным и минимальным значением дробной части элементов.
# in                                             in
# >> 3                                           >> 4

# out                                            >> out
# >> [2.84, 9.42, 1.87]                          >> [4.83, 9.91, 7.74, 9.39]
# >> "Min: 0.42, Max: 0.87, Difference: 0,45"    >> "Min: 0.39, Max: 0.91, Difference: 0,52"

from random import uniform

length_list = int(input('Введите длину списка вещественных чисел: '))

def random_real_number(number: int) -> list:
    real_list = []
    for i in range(number):
        real_list.append(round(uniform(0, 5), 2))
    return real_list

# print(random_real_number(length_list)) # [1.87, 2.05, 3.8, 2.7, 0.68]

def def_min_max(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f'Min: {num_min: .2f}, Max: {num_max: .2f}, Difference: {result}')
    return result

list_numbers = random_real_number(length_list)
print(list_numbers)
print(def_min_max(list_numbers))

# ** Задача № 7: ______________________________
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных чисел.
# in                                               in
# >> 8                                             >> 3

# out                                              >> out
# >> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21     >> 2 -1 1 0 1 1 2


n = int(input('Введите число ')) # 8

def num_fib(x:int) -> list:
    numbers = [0,1]
    for i in range(2, x + 1):
        numbers.append(numbers[i - 1] + numbers [i - 2] )

    not_numbers = []
    for i in range(1, x + 1):
        not_numbers.append(numbers[-i] * (-1)**(i) )
    return not_numbers + numbers

list_fib = num_fib(n)
print(list_fib) # [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print(type(list_fib)) # <class 'list'>

#  Или...

def neg_fob(n: int) -> list:
    a, b = 1, 1
    list_num = [0]

    for item in range(n):
        list_num.append(a)
        list_num.insert(0, a * (-1) ** item)
        a, b = b, b + a
    return list_num

list_fib = neg_fob(int(input('Введите число: '))) # 8
print(list_fib) # [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

