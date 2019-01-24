# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#  При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections


def array_to_string(result):
    return ''.join(str(element) for element in result).lstrip('0') or '0'


print('Воспользуемся калькулятором для шестнадцатиричных чисел?')
print('Введите, пожалуйста, два числа, чтобы получить их результат сложения и умножения')
# Получаем пару значений от пользователя и преобразуем в очередь
number1 = collections.deque(list(input("Ваше первое шестнадцатиричное число:   ")))
number2 = collections.deque(list(input("Ваше второе шестнадцатиричное число:   ")))


# функция для уравнивания длин массивов,
# так как будем складывать в столбик, заполняем нулями те разряды, которых нет у одного массива, но есть у другого:
def equal_length(deque1, deque2):
    len1 = len(deque1)
    len2 = len(deque2)
    if len1 != len2:
        if len1 > len2:
            difference_length = len1 - len2
            for i in range(0, difference_length):
                deque2.appendleft(0)
        if len2 > len1:
            difference_length = len2 - len1
            for i in range(0, difference_length):
                deque1.appendleft(0)
    return deque1, deque2


equal_length(number1, number2)
letters_into_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


# Переделываем массивы, присваивая буквам числа:
def move_to_decimal(deque):
    nDeq = []
    for e in deque:
        nDeq.append(letters_into_numbers[str(e).upper()])
    return nDeq


eggs = move_to_decimal(number1)
eggs.reverse()
spam = move_to_decimal(number2)
spam.reverse()


# складываем поэлементно, если результат сложения меньше или равен 15, оставляем его,
# если больше 15, то вычитаем 16, остаток от вычитания складываем в результирующую позицию в массиве суммы,
# при этом прибавляем 1 к следующему элементу массива или создаем дополнительный элемент в результирующем массиве
# со значением 1,если вышли за длинну массивов, которых складываем
def summ(deque1, deque2):
    max_len = max(len(deque1), len(deque2))
    summ = [0 * i for i in range(max_len + 1)]
    for i, element1 in enumerate(deque1):
        summ[i] = summ[i] + element1
    for i, element2 in enumerate(deque2):
        summ[i] = summ[i] + element2
    for e, el in enumerate(summ):
        if el >= 15:
            summ[e + 1] = summ[e + 1] + el // 16
            summ[e] = el % 16
    return summ


numbers_into_letters = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# результирующий массив приводим к шестнадцатиричному цифро-буквенному виду:
def move_to_hexadecimal(list1):
    nDeq = []
    for e in list1:
        nDeq.append(numbers_into_letters[e])
    return nDeq


summ = summ(eggs, spam)
summ.reverse()
print(f'Результат сложения Ваших чисел: {array_to_string(move_to_hexadecimal(summ))}')


# функция под умножение
def product(deque1, deque2):
    deque1.reverse()
    deque2.reverse()
    # заводим массив под результаты умножения:
    result = [0 * i for i in range(len(deque1) + len(deque2) + 1)]
    # перебираем массивы поэлементно
    for i, element1 in enumerate(deque1):
        for j, element2 in enumerate(deque2):
            # вставлем результат умножения элементов на соответствующее разрядное место
            result[i + j] = result[i + j] + int(element1) * int(element2)
    # получился массив с числами, где есть переполнение в разрядах будущего числа
    for i, item in enumerate(result):
        if item >= 15:
            result[i + 1] = result[i + 1] + item // 16
            result[i] = item % 16
    result.reverse()
    return result


result_product = move_to_hexadecimal(product(move_to_decimal(number1), move_to_decimal(number2)))
print('Результат умножения Ваших чисел: ', end='')
print(f'{array_to_string(result_product)}')
