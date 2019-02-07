# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
#  рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием
# памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.

# Также укажите в комментариях версию Python и разрядность вашей ОС.
# Python 3.7.0
# x86_64


import sys
import random

####################################################################################################################
# Task5, HW_3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
####################################################################################################################
SIZE = 1000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
output = 'Количество памяти, выделенное под переменные: '


def get_memory(dictionary):
    total = 0
    for key in dictionary.keys():
        value = dictionary[key]
        if key != '__len__' and type(value) == int or type(value) == float or type(value) == str or type(
                value) == list or type(
            value) == set or type(value) == tuple or type(value) == dictionary:
            total = total + sys.getsizeof(value)
    return total


initial = get_memory(locals())


# 1-е решение:
def search_max_negative_1(list_init):
    list_negative = []
    for i in list_init:
        if i < 0:
            list_negative.append(i)
    min_item = abs(list_negative[0])
    for i in list_negative:
        if abs(i) < min_item:
            min_item = abs(i)
    return [- min_item, list_init.index(- min_item)], get_memory(locals())


eggs1 = search_max_negative_1(array)[1] + initial
print(f" 1-й метод. {output} {eggs1}")


# 2-е решение:
def search_max_negative_2(list_init):
    max_negative = float("-inf")

    for i in list_init:
        if i < 0:
            if i > max_negative:
                max_negative = i

    index_max_negative = list(i for i, e in enumerate(list_init) if e == max_negative)[0]

    return [max_negative, index_max_negative], get_memory(locals())


spam2 = search_max_negative_2(array)[1] + initial
print(f" 2-й метод. {output} {spam2}")


# 3-e решение:
def search_max_negative_3(list_init):
    array_negative = []
    for i in list_init:
        if i < 0:
            array_negative.append(i)
    max_negative = max(array_negative)
    index_max_negative = list(i for i, e in enumerate(list_init) if e == max_negative)[0]

    return [max_negative, index_max_negative], get_memory(locals())


eggs3 = search_max_negative_3(array)[1] + initial
print(f" 3-й метод. {output} {eggs3}")
print(f' Самый экономичный расход памяти: {min(spam2, eggs1, eggs3)}')
##########################################################################
# Результаты анализа вставьте в виде комментариев к коду.
##########################################################################
# При SIZE = 1000, элементы генерируются от -100 до 100:
#  1-й метод. Количество памяти, выделенное под переменные:  23368
#  2-й метод. Количество памяти, выделенное под переменные:  18548
#  3-й метод. Количество памяти, выделенное под переменные:  23396
#  Самый экономичный расход памяти: 18548, во втором методе решения задачи.

# При SIZE = 10, элементы генерируются от -3 до 10:
#  1-й метод. Количество памяти, выделенное под переменные:  952
#  2-й метод. Количество памяти, выделенное под переменные:  884
#  3-й метод. Количество памяти, выделенное под переменные:  980
#  Самый экономичный расход памяти: 884, во втором методе решения задачи.
#########################################################################
# Также укажите в комментариях версию Python и разрядность вашей ОС.
# Python 3.7.0
# x86_64
#########################################################################
