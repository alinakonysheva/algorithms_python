# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# заводим тестовый массив
list_int = [0, 3, 5, 6, -6, 4, 2, 13, 9, 56, 24, -10]

# заводим листы под максимальный и минимальный элемент и их индексы
max_element = [0, list_int[0]]
min_element = [0, list_int[0]]

# ищем по всему массиву максимальный и минимальный элемент
for i in range(len(list_int)):
    if list_int[i] > max_element[1]:
        max_element = [i, list_int[i]]
    if list_int[i] < min_element[1]:
        min_element = [i, list_int[i]]

# вставляем максимальный элемент на место минимального
list_int.insert(min_element[0], max_element[1])
# удаляем минимальный с его места
list_int.pop(min_element[0]+1)
# вставляем минимальный элемент на место максимального
list_int.insert(max_element[0], min_element[1])
# удаляем максимальный элемент с его места
list_int.pop(max_element[0]+1)


print(list_int)
