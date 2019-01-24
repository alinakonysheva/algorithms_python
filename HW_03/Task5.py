# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


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

    return - min_item, list_init.index(- min_item)


eggs = search_max_negative(array)
print(f" Максимальное отрицательный элемент в массиве: {eggs[0]}")
print(f" Место максимального отрицательного элемента в массиве: {eggs[1]}")

# поменять алгоритм
