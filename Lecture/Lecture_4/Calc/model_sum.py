# Создали модель калькулятора, в рамках которого есть данные, инициализация данных и логика  действия.
# есть два числа
x = 0
y = 0


# есть метод инициализации переменных x и y
def init(a, b):
    global x  # инициализировал переменную x в контексте метода
    global y  # инициализировал переменную y в контексте метода
    x = a
    y = b

# есть метод действия переменных x и y. Данном контексте складывание.
def do_it():
    return x + y
