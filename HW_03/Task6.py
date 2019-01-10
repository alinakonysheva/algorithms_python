# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# заводим листы под максимальный и минимальный элемент и их индексы
max_item = [0, array[0]]
min_item = [0, array[0]]
# ищем по всему массиву максимальный и минимальный элемент
for i in range(len(array)):
    if array[i] > max_item[1]:
        max_item = [i, array[i]]
    if array[i] < min_item[1]:
        min_item = [i, array[i]]
print(f' максимальный элемент - {max_item[1]}, минимальный элемент - {min_item[1]}')
print(f' между элементами стоит {abs(max_item[0] - min_item[0]) - 1} элементов(а)')

summ = 0
if min_item[0] > max_item[0]:
    for i in range(min_item[0], max_item[0]):
        summ = summ + array[i]
    print(f' Сумма от максимального до минимального элемента (не включая минимальный и максимальный) = {summ}')
else:
    for i in range(max_item[0], min_item[0]):
        summ = summ + array[i]
    print(f' Сумма от максимального до минимального элемента (не включая минимальный и максимальный) = {summ}')

