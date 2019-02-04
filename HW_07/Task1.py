# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
#  Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

# Проверим на умность, сравним реализацию алгоритма из лекции с альтернативной:
import timeit
# python -m timeit -n 100 -s "import Task1" "Task1.bubble1([-19, 0, -20, 40, 49, -15, 98, 80, 12])"
# python -m timeit -n 100 -s "import Task1" "Task1.bubble1([-70, -90, 0, 56, -49, 5, -98, 24, 67])"
# 100 loops, best of 5: 15.1 usec per loop
# 100 loops, best of 5: 12.6 usec per loop

# python -m timeit -n 100 -s "import Task1" "Task1.bubble1([-19, 0, -20, 40, 49, -15, 98, 80, 12])"
# 100 loops, best of 5: 11.8 usec per loop
# python -m timeit -n 100 -s "import Task1" "Task1.bubble1([-70, -90, 0, 56, -49, 5, -98, 24, 67])"
# 100 loops, best of 5: 14.6 usec per loop
# Вывод по времени: альтернативное решение не сильно умнее.

# Проверим на умность по памяти, последнее число указывает на занимаемую память:
#[21, 58, 31, -46, 15, 76, -84, 98, -39, -89]
# ([-89, -84, -46, -39, 15, 21, 31, 58, 76, 98], 244)
# ([-89, -84, -46, -39, 15, 21, 31, 58, 76, 98], 244)
# Вывод по памяти:не особо умнее тоже.

import random
import sys

array1 = [random.randint(-100, 100) for _ in range(10)]
print(array1)

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


def bubble1(li):
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li, get_memory(locals())


print(bubble1(array1))


def bubble2(li):
    for n in range(len(li) - 1, 0, -1):
        for i in range(n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]

    return li, get_memory(locals())


print(bubble2(array1))

