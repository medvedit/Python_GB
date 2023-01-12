#  Ускоренная обработка данных: lambda, filter, map, zip, enumerate, List Comprehension
# ______________________________________________________________________________________________________

#  lambda : -----------------

def f(x):
    return x**2
# Можем положить функцию в переменную:
g = f # Переменная, которая хранит ссылку на функцию.
print(type(f)) # <class 'function'>
print(type(g)) # <class 'function'>
# Вызывать как функцию, так и переменную:
print(f(4)) # 16
print(g(4)) # 16

# Далее...
# С одной переменной:

def calc_1(x):
    return x + 10


def calc_2(x):
    return x * 10

def math(op, x):
    print(op(x))

math(calc_2, 10) # 100
math(calc_1, 10) # 20

# Далее...
# С двумя переменными:

# def sum(x, y):
#     return x + y

sum = lambda x, y : x +y

f = sum

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(mult, 4, 5) # 20
calc(f, 4, 5) # 9
calc(sum, 6, 9) # 15
calc(lambda x, y : x + y +3, 4, 5) # 12


# Создаём список:
# List Comprehension: # Понимание списка:

# [exp for item in iterable] # exp для элемента в итерации
# [exp for item in iterable (if conditional)] # exp для элемента в итерации (если условно)
# [ exp <if conditional> for item in iterable (if conditional)] # exp <если условно> для элемента в итерации (если условно)

list_1 = []
for i in range(1, 11):
    if i%2 == 0:
        list_1.append(i)

print(list_1) # [2, 4, 6, 8, 10]

# Или...

list_1 = [i for i in range(1, 16)]
print(list_1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# + проверка на четность:

list_1 = [i for i in range(1, 16) if i%2 == 0]
print(list_1) # [2, 4, 6, 8, 10, 12, 14]

# + Вывод картежем:

list_1 = [(i, i) for i in range(1, 16) if i%2 == 0]
print(list_1) # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14)]

# еще применение:

def f(x):
    return x**3

list_1 = [f(i) for i in range(1, 16) if i%2 == 0]
print(list_1) # [8, 64, 216, 512, 1000, 1728, 2744]

# Или :

list_1 = [(i, f(i)) for i in range(1, 16) if i%2 == 0]
print(list_1) # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744)] # Число и его куб

# Задача№ 1:
# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа). Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

def f(x):
    return x**2

list_1 = [(i, f(i)) for i in (1, 2, 3, 5, 8, 15, 23, 38) if i%2 == 0]
print(list_1) # [(2, 4), (8, 64), (38, 1444)]

#  решение от Сергея:

path = '/Users/Medwed_SA/Desktop/Education/Python/Знакомство с языком Python/Lecture_end_Seminare/Python_GB/Lecture/file_1.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for i in numbers:
    if not i % 2:
        out.append((i, i**2))

print(out) # [(2, 4), (8, 64), (38, 1444)]






