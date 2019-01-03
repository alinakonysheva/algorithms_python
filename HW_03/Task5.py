# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

list_init2 = [3, -0.9, 6, -6, 4, 5, 13, 9, -0.56, 24, -16, 5, -965, 85, 0]

# заводим функцию, которая вернет минимальный элемент и позицию в массиве


def search_max_negative(list_init):
    list_negative = []
    # создаем массив отрицательных элементов
    for i in list_init:
        if i < 0:
            list_negative.append(i)
    # ищем минимальный по модулю элемент массива
    min_item = abs(list_negative[0])
    for i in list_negative:
        if abs(i) < min_item:
            min_item = abs(i)

    return -min_item, list_init.index(-min_item)


print(f" Максимальное отрицательный элемент в массиве: {search_max_negative(list_init2)}")
