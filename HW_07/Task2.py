# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

array = [random.randint(0, 50) for _ in range(8)]
print(f'Исходный массив: {array}')


def merge_sort(lst):
    # первый шаг алгоритма сортировки слиянием -- разделить массив на массивы единичных длин:
    if len(lst) > 1:
        # поэтому до тех пор, пока есть куски длиной больше единицы: делим пополам и формируем списки из половин
        middle = len(lst) // 2
        lefthalf = lst[:middle]
        righthalf = lst[middle:]
        # которые снова делим пополам
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # второй шаг алгоритма сортировки слияния: сравнение ближайших массивов и запись в результирующий массив
        # счетчик для перебора левой половины
        i = 0
        # счетчик для перебора правой половины
        j = 0
        # счетчик мест в финальном массиве
        f = 0
        # до тех пор, пока мы не вышли за длины массивов:
        while i < len(lefthalf) and j < len(righthalf):
            # сравниваем поэлементно:
            if lefthalf[i] < righthalf[j]:
                # и записываем меньший элемент в финальный массив первым:
                lst[f] = lefthalf[i]
                i = i + 1
            else:
                lst[f] = righthalf[j]
                j = j + 1
            f = f + 1
        # дозапишем в финальный массив оставшиеся бOльшие:
        while i < len(lefthalf):
            lst[f] = lefthalf[i]
            i = i + 1
            f = f + 1

        while j < len(righthalf):
            lst[f] = righthalf[j]
            j = j + 1
            f = f + 1
    return lst


print(f'Отсортированный массив: {merge_sort(array)}')
