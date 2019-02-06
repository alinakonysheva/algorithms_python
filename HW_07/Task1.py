# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

# Проверим на умность, сравним доработанную реализацию алгоритма из лекции (1 вариант) с немного измененной
# лекционной (2 вариант) по двум показателям, немножко по памяти и по времени
import cProfile
import random
import sys

array1 = [random.randint(-100, 100) for _ in range(10)]
print(f'Входной массив: {array1}')
print('#' * 50)
array2 = array1.copy()


def get_memory(dictionary):
    total = 0
    for key in dictionary.keys():
        value = dictionary[key]
        if key != '__len__' and type(value) == int or type(value) == float or type(value) == str or type(
                value) == list or type(
            value) == set or type(value) == tuple or type(value) == dictionary:
            total = total + sys.getsizeof(value)
    return total


initial = get_memory(locals())


def bubble1(lst):
    n = 1
    permutation = True
    while n < len(lst) and permutation:
        permutation = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                permutation = True
        n += 1
    sorted_li = lst
    return f'{sorted_li}, занимаемая память: {get_memory(locals())}'


print('Первый вариант сортировки: ')
print(bubble1(array1))
print('#' * 100)

# "умность" этой реализации идентична "умности" того, что было дано на лекции
def bubble2(lst):
    for n in range(len(lst) - 1, 0, -1):
        for i in range(n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    sorted_li = lst
    return f'{sorted_li}, занимаемая память: {get_memory(locals())}'


print('Второй вариант сортировки: ')
print(bubble2(array2))
print('#' * 100)

cProfile.run('bubble1(array1)')
cProfile.run('bubble2(array2)')
# Оцениваем умность:
# Заметная разница во времени начинается с длины входного массива пордяка 10**3:
# Первый вариант: 14 function calls in 0.001 seconds, на два порядка быстрее, но занимаемая память чуть больше 18104
# Второй вариант: 12 function calls in 0.079 seconds, медленнее, память экономичнее память 16180
# Гигантская разница во времени с длиной входного массива пордяка 10**4:
# Первый вариант: 14 function calls in 0.003 seconds, на 4 порядка быстрее второго варианта
# Второй вариант: 12 function calls in 7.664 seconds
