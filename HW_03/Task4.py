# 4. Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# заводим словарь
counter_items = {}
# заводим переменные под максимальное значение счетчика и максимальный элемент
max_count = 0
max_item = None

# перебираем значения элементов массива
for i in array:
    # в словарь складываем: в ключи -- элементы массива, а в значения -- количество упоминаний в массиве
    if i in counter_items:
        counter_items[i] = counter_items[i] + 1
    else:
        counter_items[i] = 1
    # попутно ищем максимально часто встречающийся элемент
    if counter_items[i] > max_count:
        max_count = counter_items[i]
        max_item = i

print(f"Самый часто встречающийся элемент в массиве это -- {max_item}, встречается {max_count} раз(а)")
