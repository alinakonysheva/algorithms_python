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
dict_sixteen = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


# переводим все в цифрое значение
def move_to_decimal(deque):
    deque_only_decimal = deque.copy()
    for i, element in enumerate(deque):
        if ord(str(element)) > ord('9'):
            deque_only_decimal.insert(i, dict_sixteen[element.upper()])
            del deque_only_decimal[i + 1]
    return deque_only_decimal


print(f' Приводим все к цифрам первое число: {move_to_decimal(number1)}')
print(f' Приводим все к цифрам второе число: {move_to_decimal(number2)}')


# переворачиваем поэлементно, чтобы использовать дальше:
def reversing(deque):
    deque.reverse()
    eggs = deque
    return eggs


print(f' Переворачиваем первое {reversing(move_to_decimal(number1))}')
print(f' Переворачиваем второе {reversing(move_to_decimal(number2))}')


# складываем поэлементно, если результат сложения меньше или равен 9, оставляем его,
# если больше 9 и меньше 16 -- присваиваем букву, если больше 16, то вычитаем 16, и присваиваем значение
# по этой же технике, при этом перебрасывая 1 на следующий элемент
def summ():
    pass

# переворачиваем массивы для удобства работы со степенями
# def reverse(deque1, deque2):
#   deque1_reversed = deque1.reverse()
#   deque2_reversed = deque2.reverse()
#    return deque1_reversed, deque2_reversed


# print(reverse(number1, number2))

# def turn_into_numeral(deque1_reversed, deque2_reversed):
#    for i, element in enumerate(deque1_reversed):
#       if element > 9:


# def move_to_decimal(deque1_reversed):
# for i in range(0, len(deque1_reversed)):
# d['1']
