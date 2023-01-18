# Задача 1: ___________________________________________________________
# Создайте список из N натуральных чисел, упорядоченных по возрастанию.
# Среди чисел не хватает одного, чтобы выполнить условие A[i] - 1 = A[i - 1].
# Найдите это число.

from random import choice


sl = int(input('Введите длину списка: '))

def sl_list(number:int) ->list:
    out_list = [x for x in range(number + 1)]
    out_list.remove(choice(out_list))
    return out_list
z = sl_list(sl)
print(z)

def search_pass(in_list):
    for i in range(1,len(in_list)):
        if in_list[i] - 1 != in_list[i - 1]:
            return in_list[i] - 1
    return -1

print(search_pass(z))

# Задача 2: ___________________________________________________________
# Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя

from random import choices

def random_list_length_user() -> list:
    length = int(input('Введите длину списка: '))
    sl = choices(range(length * 2), k=length)
    return sl

generated_list = random_list_length_user()
print(generated_list)

def ascending_sequence(in_list: list) -> list:
    out_list = []
    for i in range(len(in_list)):
        temp = in_list[i]
        temp_list = [temp]
        for j in range(i + 1, len(in_list)):
            if in_list[j] > temp:
                temp = in_list[j]
                temp_list.append(temp)
        if len(temp_list) > 1:
            out_list.append(temp_list)
    return out_list

print(ascending_sequence(generated_list))


#__________________________________________________________________________ Домашняя работа __________________________________________________________________________

# Напишите программу удаляющую из текста все слова содержащие "абв". в тексте разделителем является пробел.


from random import sample

num = int(input('Введите длину, количество слов в тексте: '))
txt = 'ваб' # буквы для создания случайных слов, комбинаций.
search = 'абв' # это сочетание ищем и удаляем.

def form_a_string(word_count: int, text: str) -> str:
    f_list = []
    for i in range(word_count):
        temp_list = sample(text, k=len(text))
        f_list.append("".join(temp_list))
    out_text = " ".join(f_list)
    return out_text

fin_word = form_a_string(num, txt)
print(fin_word)

def search_match_remove(in_text: str, search_text: str) -> str:
    checked_text = [i for i in in_text.split() if search_text not in i]
    out_text = " ".join(checked_text)
    return out_text

print(search_match_remove(fin_word, search))

