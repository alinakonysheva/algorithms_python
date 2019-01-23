# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#  При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections

print('Воспользуемся калькулятором для шестнадцатиричных чисел?')
print('Введите, пожалуйста, два числа, для того, чтобы получить их результат сложения и умножения')
# получаем пару значений от пользователя и преобразуем в очередь
number1 = collections.deque(list(input("Ваше первое шестнадцатиричное число:   ")))
number2 = collections.deque(list(input("Ваше второе шестнадцатиричное число:   ")))


# print(number1, number2)


# функция для уравнивания длин массивов use extendleft(iterable)
def equal_length(deque1, deque2):
    if len(deque1) != len(deque2):
        if len(deque1) > len(deque2):
            difference_length = len(deque1) - len(deque2)
            for i in range(0, difference_length):
                deque2.appendleft(0)
        if len(deque2) > len(deque1):
            difference_length = len(deque2) - len(deque1)
            for i in range(0, difference_length):
                deque1.appendleft(0)
    return deque1, deque2


print(equal_length(number1, number2))
letters_into_numbers = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


# переводим все в цифрое значение
def move_to_decimal(deque):
    deque_only_decimal = deque.copy()
    for i, element in enumerate(deque):
        if ord(str(element)) > ord('9'):
            deque_only_decimal.insert(i, letters_into_numbers[element.upper()])
            del deque_only_decimal[i + 1]
    return deque_only_decimal


print(f' Приводим все к цифрам первое число: {move_to_decimal(number1)}')
print(f' Приводим все к цифрам второе число: {move_to_decimal(number2)}')


# переворачиваем поэлементно, чтобы использовать дальше:
def reversing(deque):
    deque.reverse()
    eggs = deque
    return eggs


eggs = reversing(move_to_decimal(number1))
spam = reversing(move_to_decimal(number2))
print(f' Переворачиваем первое {eggs}')
print(f' Переворачиваем второе {spam}')


# складываем поэлементно, если результат сложения меньше или равен 9, оставляем его,
# если больше 9 и меньше 16 -- присваиваем букву, если больше 16, то вычитаем 16, и присваиваем остатку значение
# по освоенной сверху методе, при этом перебрасывая 1 на следующий элемент
# как перебросить на другой элемент 1?
def summ(deque1, deque2):
    summ = []
    for i, element1 in enumerate(deque1):
        for j, element2 in enumerate(deque2):
            if i == j:
                sum_element = int(element1) + int(element2)
                if sum_element <= 15:
                    summ.append(sum_element)
                else:
                    sum_element = sum_element - 16
                    summ.append(sum_element)
                    if i != len(deque1) - 1:
                        deque1[i + 1] = int(deque1[i + 1]) + 1
                    else:
                        summ.append(1)
    return summ


numbers_into_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def move_to_hexadecimal(list1):
    list_hex = list1.copy()
    for i, element in enumerate(list1):
        if element > 9:
            list_hex.insert(i, numbers_into_letters[element])
            del list_hex[i + 1]
    return list_hex

print(f'Результат сложения Ваших чисел: {move_to_hexadecimal(reversing(summ(eggs, spam)))}')
