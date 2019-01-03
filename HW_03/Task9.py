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
MAX_ITEM = 10
array = [[random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE1)] for j in range(SIZE2)]
for i in array:
    print(str(i), end=' ' )
