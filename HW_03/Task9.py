# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# матрица с максимальным элементом среди минимальных -- 7
# matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def search_max_from_min(matrix):

# max_j_in_i = 0

# print(matrix_1[0][1])

import random

SIZE1 = 3
SIZE2 = 3
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE1)] for j in range(SIZE2)]

print("Матрица и минимальный элемент в каждом столбце:")
for line in matrix:
    for i, j in enumerate(line):
        print(f'{j:>5}', end='')
    print('  ')
set_min = []
for i in range(SIZE2):
    min_in_column = matrix[0][i]
    for j in range(SIZE1):
        if matrix[j][i] < min_in_column:
            min_in_column = matrix[j][i]
    set_min.append(min_in_column)
    print(f'{min_in_column:>5}', end='')

max_in_line = set_min[0]
for i in set_min:
    if i > max_in_line:
        max_in_line = i
print('\n')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_in_line}')

