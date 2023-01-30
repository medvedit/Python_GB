'''Вычислить значение выражений:
12 + 5
12 / 6
112 * 2

1. Где операторы?
2. Где числовые значения?

Уровень №1
- 1 аргумент
- 2 действия

12 + 5

Уровень №2
- Количество действий произвольно
- количество аргументов произвольно

12 + 5 - 3 ...

Уровень №3
- Действия имеют приоритет

12 - 5 * 3

Уровень №4
- Действия разделяются скобками

(120 - 20) * 2                  '''


# Уровень №1 ______________________________________________________________________________________________________________

# t = '22 + 3' # на вход строка.
# m = t.split()
# print(m) # ['22', '+', '3']
#          #   0     1    2  индексы.
# a = int(m[0]) # '22'
# c = m[1] #      '+'
# b = int(m[2]) # '3'

# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     print(a / b)
# elif c == '*':
#     print(a * b)

# # Уровень №2 _______________________________________________________________________________________________________________

# t = '22 + 300 - 14 + 2 + 11' # на вход строка.
# m = t.split()

# a = int(m[0])
# c = m[1]
# b = int(m[2])
# print(m)


# def exp_eval(al, bl, ch):
#     if ch == '+':
#         return al + bl
#     elif ch == '-':
#         return al - bl
#     elif ch == '/':
#         return al / bl
#     elif ch == '*':
#         return al * bl

# result = exp_eval(a, b, c)
# print(result)

# for i in range(3, len(m) - 1, 2):
#     result = exp_eval(result, int(m[i+1]), m[i])
#     print(m[i], int(m[i+1]))
#     print(result)


# # Или упрощаем ..............................................

# str_t = '22 + 300 - 14 + 2 + 11' # на вход строка.
# str_m = str_t.split()

# first_num = int(str_m[0])

# def exp_eval(a, b, sign):
#     if sign == '+':
#         return a + b
#     elif sign == '-':
#         return a - b
#     elif sign == '/':
#         return a / b
#     elif sign == '*':
#         return a * b

# def ttt(int_num, str_in):
#     for i in range(1, len(str_in) - 1, 2): # с элемента на индексе 1, до элемента на индексе len(str_in) - 1, с шагом 2
#         int_num = exp_eval(int_num, int(str_in[i+1]), str_in[i])
#         print(str_in[i], int(str_in[i+1]))
#     return int_num

# print(ttt(first_num, str_m))



 # Уровень №3 _____________________________________________________________________________________________________________


str_t = '22 * 300 - 14 + 2 * 11 + 2 - 3000 / 100' # на вход строка.
str_m = str_t.split()


def exp_eval(a, b, sign): # Блок арифметических команд.
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '/':
        return a / b
    elif sign == '*':
        return a * b


''' Доделал решение для работы на семинаре. '''

def action_priority(list_m:list) -> list: # вычисления по приоритету (знак * или / ).
    first_num = int(list_m[0])
    new_list_m = []
    for i in range(1, len(list_m) - 1, 2):
        if list_m[i] == '*' or list_m[i] == '/':
            if not new_list_m:                                    # Если список пуст, то добавляем значения.
                first_num = exp_eval(int(list_m[i - 1]), int(list_m[i+1]), list_m[i])
                new_list_m.append(first_num)
            else:
                new_list_m.pop(-1)                               # Иначе вначале удаляем последние значение.
                first_num = exp_eval(int(list_m[i - 1]), int(list_m[i+1]), list_m[i])
                new_list_m.append(first_num)
        else:
            new_list_m.append(list_m[i])
            new_list_m.append(list_m[i+1])
    return new_list_m




def simple_calculation(list_values:list) -> int: # Линейное вычисление (знак + или - ).
    int_num = int(list_values[0])
    for i in range(1, len(list_values) - 1, 2):
            int_num = exp_eval(int_num, int(list_values[i+1]), list_values[i])
    return int_num


first_treatment = action_priority(str_m)
print(f'Ответом к примеру {str_t} = {simple_calculation(first_treatment)} с учетом всех приоритетов.')

 # Ответом к примеру 22 * 300 - 14 + 2 * 11 + 2 - 3000 / 100 = 6580 с учетом все приоритетов.


# Уровень №4 _____________________________________________________________________________________________________________

'''Это решение было создано на основании просмотренного видео https://youtu.be/Vk-tGND2bfc'''


expression = "(1 + 4) * (5 * (10 - 2)) / 5 + 87 * (8 + 6 * 9^2)"


def expand_expression(expression_string_input):

    ACTIONS = {'+': (1, lambda x, y: x + y),
               '-': (1, lambda x, y: x - y),
               '*': (2, lambda x, y: x * y),
               '/': (2, lambda x, y: x / y),
               '^': (3, lambda x, y: x ** y)
               }

    digits_stack = [] # Создали пустой стек для цифр.
    symbols_stack = [] # Создали пустой стек для символов.

    expression_string = expression_string_input # Создал копию строки для красивого вывода в конце решения.

    expression_string = expression_string.replace('+', ' + ') # Создаем пробелы между символами, если во входящем тексте их нет.
    expression_string = expression_string.replace('-', ' - ')
    expression_string = expression_string.replace('*', ' * ')
    expression_string = expression_string.replace('/', ' / ')
    expression_string = expression_string.replace('(', ' ( ')
    expression_string = expression_string.replace(')', ' ) ')
    expression_string = expression_string.replace('^', ' ^ ')
    data_after_split = expression_string.split() # Создали list строк из всего выражения.


    for symbol in data_after_split: # Проходим по всей строке пока не закончатся символы.
        if symbol.isdigit(): # Если число, то
            digits_stack.append(int(symbol)) # добавляем в стек чисел.
        elif symbol in ACTIONS: # Или символ из ACTIONS ...
            if len(symbols_stack) == 0: # Если стек символов пуст, то
                symbols_stack.append(symbol) # добавляем найденный символ в стек символов.
                continue # Возврат в первый цикл for.
            if symbols_stack[-1] == '(': # Если крайний элемент в стеке равен '(', то
                symbols_stack.append(symbol) # то добавляем в стек символов тот символ, на который сейчас "смотрим".
                continue # Возврат в первый цикл for.

            while symbols_stack: # пока мы в стеке символов ...
                if ACTIONS.get(symbol)[0] < ACTIONS.get(symbols_stack[-1])[0]: # если символ на который сейчас "смотрим",
                                                                                # меньше приоритетом крайнего символа в стеке символов, то..
                    y, x = digits_stack.pop(), digits_stack.pop() # забираем из стека цифр крайние две цифры
                    digits_stack.append(ACTIONS[symbols_stack[-1]][1](x, y))# и после выполнения действия,
                                                                            # на основании крайнего знака из стека символов,
                                                                            # в описанном действии ACTIONS -> кладем
                                                                            # результат действия обратно в стек цифр.
                    del symbols_stack[-1] # после этого удаляем крайний символ из стека символов.

                elif ACTIONS.get(symbol)[0] == ACTIONS.get(symbols_stack[-1])[0]: #если символ на который сейчас "смотрим",
                                                                                # равен приоритетом крайнему символу в стеке символов, то..
                    y, x = digits_stack.pop(), digits_stack.pop() # забираем из стека цифр крайние две цифры
                    digits_stack.append(ACTIONS[symbols_stack[-1]][1](x, y)) # и после выполнения действия,
                                                                            # на основании крайнего знака из стека символов,
                                                                            # в описанном действии ACTIONS -> кладем
                                                                            # результат действия обратно в стек цифр.
                    del symbols_stack[-1] # после этого удаляем крайний символ из стека символов.

                else:
                    symbols_stack.append(symbol) # После всех манипуляций, добавляем символ на который сейчас "смотрим" в стек символов.
                                                # либо приоритет символа на который мы сейчас "смотрим" больше приоритета
                                                # крайнего символа в стеке символов.
                break # принудительно прерываем работу цикла while

        elif symbol == ')': # Если тот символ, на который мы сейчас смотрим равен  ')', то
            while symbols_stack[-1] != '(': # пока крайний символ в стеке символов НЕ РАВЕН '('
                y, x = digits_stack.pop(), digits_stack.pop() # забираем из стека цифр крайние две цифры
                digits_stack.append(ACTIONS[symbols_stack[-1]][1](x, y)) # и после выполнения действия,
                                                                        # на основании крайнего знака из стека символов,
                                                                        # в описанном действии ACTIONS -> кладем
                                                                        # результат действия обратно в стек цифр.
                del symbols_stack[-1] # после этого удаляем крайний символ из стека символов.
            if symbols_stack[-1] == '(': # если крайний символ в стеке символов равен  '(', то
                del symbols_stack[-1] # удаляем крайний символ из стека символов.
        else:
            symbols_stack.append(symbol) # иначе добавляем символ в стек символов.

    while len(symbols_stack) > 0: # Пока стек символов не пуст...
        y, x = digits_stack.pop(), digits_stack.pop() # берем крайние две цифры
        digits_stack.append(ACTIONS[symbols_stack[-1]][1](x, y)) # делаем действие на основании крайнего символа
        del symbols_stack[-1] # удаляем крайний символ

    result = digits_stack.pop() # конечное число в результат.

    print(expression_string_input + ' = ' + str(result)) # ФСЁ . . .

    # (1 + 4) * (5 * (10 - 2)) / 5 + 87 * (8 + 6 * 9^2) = 42983


expand_expression(expression)



 # ИЛИ ____________________________________________________________________________________________________________


''' Это РЕШЕНИЕ НЕ МОЁ !!! '''

import re

expression = "( 1 + 4 ) * ( 5 * 7 - ( 10 - 2 ))"

ACTIONS = {
            "^": lambda x, y: str(float(x)**float(y)),
            "*": lambda x, y: str(float(x) * float(y)),
            "/": lambda x, y: str(float(x) / float(y)),
            "+": lambda x, y: str(float(x) + float(y)),
            "-": lambda x, y: str(float(x) - float(y))
            }

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expression: str) -> str:

    while (match := re.search(priority_reg_exp, expression)):
        expression: str = expression.replace(
            match.group(0), my_eval(match.group(1)))

    for symbol, action in ACTIONS.items():
        while (match := re.search(action_reg_exp.format(symbol), expression)):
            expression: str = expression.replace(
                match.group(0), action(*match.groups()))

    return expression

print(my_eval(expression))  #  167.0

