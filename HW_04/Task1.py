# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
# задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Task5, HW_3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# 1-е решение:
import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def search_max_negative(list_init):
    list_negative = []
    for i in list_init:
        if i < 0:
            list_negative.append(i)
    min_item = abs(list_negative[0])
    for i in list_negative:
        if abs(i) < min_item:
            min_item = abs(i)

    return - min_item, list_init.index(- min_item)


eggs = search_max_negative(array)
print(f" 1-й метод. Максимальный отрицательный элемент в массиве: {eggs[0]}")
print(f" 1-й метод. Место максимального отрицательного элемента в массиве: {eggs[1]}")

# 2-е решение:
def search_max_negative(list_init):

    return
max_negative = float("-inf")

for i in array:
    if i < 0:
        if i > max_negative:
            max_negative = i
print(f" 2-й метод. Максимальный отрицательный элемент в массиве: {max_negative}")
print(" 2-й метод. Место максимального отрицательного элемента в массиве: ", end='')
print(f"{list(i for i, e in enumerate(array) if e == max_negative)[0]}")

# 3-e решение:
array_negative = []
for i in array:
    if i < 0:
        array_negative.append(i)
max_negative = max(array_negative)
print(f" 3-й метод. Максимальный отрицательный элемент в массиве: {max_negative}")
print(f"{list(i for i, e in enumerate(array) if e == max_negative)[0]}")

