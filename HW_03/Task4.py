# 4. Определить, какое число в массиве встречается чаще всего.

list_init = [3, 0, 0, 0, 6, -6, 4, 5, 13, 9, 56, 24, -10, 5, 5, 5, 0, 0]

# заводим словарь
counter_elements = {}
# заводим переменные под максимальное значение счетчика и максимальный элемент
max_count = 0
max_item = None

# перебираем значения массива
for i in list_init:
    # в словарь складываем в ключи -- элементы массива, а в значения -- количество упоминаний в массиве
    if i in counter_elements:
        counter_elements[i] = counter_elements[i] + 1
    else:
        counter_elements[i] = 1
    # попутно ищем максимально часто встречающийся элемент
    if counter_elements[i] > max_count:
        max_count = counter_elements[i]
        max_item = i

print(f"Самый часто встречающийся элемент в массиве это {max_item}, встречается {max_count} раз(а)")

