# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# заводим тестовый массив
import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
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

# вставляем максимальный элемент на место минимального
array.insert(min_item[0], max_item[1])
# удаляем минимальный с его места
array.pop(min_item[0] + 1)
# вставляем минимальный элемент на место максимального
array.insert(max_item[0], min_item[1])
# удаляем максимальный элемент с его места
array.pop(max_item[0] + 1)

print(array)
