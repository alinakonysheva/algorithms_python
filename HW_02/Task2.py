# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input("Введите, пожалуйста, натуральное число   "))
evens = 0
odds = 0

# Заводим цикл, который будет считать четные и нечетные цфиры до тех пор,
# пока не переберем все цифры числа

while number > 0:
    number_without_last = int(number/10)
    last_numeral = number - 10 * number_without_last

    if last_numeral % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1

    number = number_without_last

print("Количество четных цифр во введенном числе: ", evens)
print("Количество нечетных цифр во введенном числе: ", odds)

