# Задача №9.
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input:       5
# Output:    120
import random
num = int(input())


def Factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(Factorial(num))

# Задача №11
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число - 1.

# Input:     5
# Output:  6
num_fb = int(input('Введите число фибоначчи: '))


def fibonache(n):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 каждое число фибоначчи
    # 1  2  2  4  5  6  7  8   9   10  11  12  13   14   15  порядковый номер числа фибоначчи
    if n == 0:
        return 1
    if n == 1:
        return 2
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1


print(
    f'Порядковый номер в системе Фибоначчи числа {num_fb} равен {fibonache(num_fb)}')

# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней(1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 - 40 50 10 - 10
# Output: 2


def Get_Number():
    while True:
        get_number = input('Введите целое, положительное от 1 до 100 число: ')
        if get_number.isdigit():
            fin_number = int(get_number)
            if fin_number == 0:
                fin_number += 1
                return fin_number
            if fin_number <= 1 or fin_number <= 100:
                return fin_number


amount_days = Get_Number()
m = []
count = 0
max = 0
for i in range(0, amount_days):
    random_number = round(random.randint(-50, 50,))
    m.append(random_number)
    if random_number < 0:
        count = 0
    if random_number > 0:
        count += 1
        if count > max:
            max = count

print(m)
print(max)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.


def Get_Number():
    while True:
        get_number = input('Введите целое, положительное от 1 до 100 число: ')
        if get_number.isdigit():
            fin_number = int(get_number)
            if fin_number == 0:
                fin_number += 1
                return fin_number
            if fin_number <= 1 or fin_number <= 100:
                return fin_number


number_of_watermelon = int(Get_Number())


def from_random_large_and_small_number(x):
    watermelon_weight = []
    import random
    for i in range(0, number_of_watermelon):
        random_number = round(random.randint(5000, 30001,))
        watermelon_weight.append(random_number)
    print(watermelon_weight)
    min = max = watermelon_weight[0]
    for i in watermelon_weight:
        if min > i: min = i
        elif max < i: max = i
    return min, max


print(from_random_large_and_small_number(number_of_watermelon))


# ===================================================================================================================== Домашнее задание Семинар ===============================================================================================================================

# Задача 10 ----------------------------------------
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и
# той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

def Get_Number():
    while True:
        get_number = input('Введите целое, положительное от 1 до 100 число: ')
        if get_number.isdigit():
            fin_number = int(get_number)
            if fin_number == 0:
                fin_number += 1
                return fin_number
            if fin_number <= 1 or fin_number <= 100:
                return fin_number


number = int(Get_Number())


def Number_Arrey(x):
    import random
    m = []
    for i in range(0, x):
        random_number = round(random.randint(0, 1,))
        m.append(random_number)
    return m


number_array = list(Number_Arrey(number))


def Zero_Or_One(num_array):
    num0 = 0
    num1 = 0
    for i in num_array:
        if i == 0:
            num0 += 1
        if i == 1:
            num1 += 1
    if num0 > num1:
        print(f'{number} -> {number_array} \nЦифры 1 меньше, её всего {num1}шт.')
    elif num0 == num1:
        print(f'{number} -> {number_array} \nКоличество 0 и 1 совпадает, их по {num0}шт.')
    else:
        print(f'{number} -> {number_array} \nЦифры 0 меньше, её всего {num0}шт.')


Zero_Or_One(number_array)


# Задача 12 -------------------------------------------------
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
for x in range(0, 1001):
    y = s - x
    if x <= y and x * y == p:
        print(x, y)
        break


# Задача 14 ---------------------------------------------------
# Требуется вывести все целые степени двойки(т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
m = 1
while m < n:
    if (m * 2 > n):
        break
    else:
        m = m * 2
        print(m)
        # print(m, end= ' ') Можно написать вывод так, но не смог убрать в конце вывода зна % (не нашел решение),
        #                    но зато изучил 'end=' .
