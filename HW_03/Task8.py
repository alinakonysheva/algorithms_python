# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import random

SIZE1 = 4
SIZE2 = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix1 = [[random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE1)] for j in range(SIZE2)]

# выводим матрицу
print("_______Матрица______")
print('____________________')
for line in matrix1:
    for i, j in enumerate(line):
        print(f'{j:>5}', end='')
    print('  ')
print('____________________')