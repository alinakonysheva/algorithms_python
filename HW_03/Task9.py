# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# создаем матрицу
import random

SIZE1 = 3
SIZE2 = 3
MIN_ITEM = 0
MAX_ITEM = 100
matrix1 = [[random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE1)] for j in range(SIZE2)]

# выводим матрицу
print("_____Матрица____")
print('________________')
for line in matrix1:
    for i, j in enumerate(line):
        print(f'{j:>5}', end='')
    print('  ')
print('________________')

print("Минимальные элементы в каждом столбце матрицы:")
print('________________')
# список, в который будем складывать минимальные значенения в каждом столбце
set_min = []

# перебираем столбцы
for i in range(SIZE1):
    min_in_column = matrix1[0][i]
    # построчно перебираем элементы в столбце и ищем минимальный
    for j in range(SIZE2):
        if matrix1[j][i] < min_in_column:
            min_in_column = matrix1[j][i]
    # формируем список из минимальных элементов в каждом столбце
    set_min.append(min_in_column)
    print(f'{min_in_column:>5}', end='')
# ищем максимальный элемент в списке минимальных элементов
max_in_line = set_min[0]
for i in set_min:
    if i > max_in_line:
        max_in_line = i
print('\n')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_in_line}')
