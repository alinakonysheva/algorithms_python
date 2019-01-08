# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

output_words_low = 'нижнюю границу диапазона в котором надо генерировать  --> '
output_words_high = 'верхнюю границу диапазона в котором надо генерировать  --> '
a = 1
while a != 0:
    try:
        print('Какого типа элемент нужно сгенерировать?')
        generation_type = int(input('1 -- целое число, 2 -- вещественное число, 3 -- символ? -->  '))

        if generation_type == 1:
            start_generation = int(
                input(f'Задайте целое число, {output_words_low}'))
            end_generation = int(input(f'Задайте целое число, {output_words_high}'))
            print('Ваше случайное целое число:')
            print(random.randint(start_generation, end_generation))
            a = int(input('Если хотите дальше генерировать, нажмите что-нибудь, 0 -- для выхода  '))
        elif generation_type == 2:
            start_generation = float(
                input(f'Задайте число, {output_words_low}'))
            end_generation = float(input(f'Задайте число, {output_words_high}'))
            print('Ваше случайное вещественное число:')
            print(random.uniform(start_generation, end_generation))
            a = int(input('Если хотите дальше генерировать, нажмите что-нибудь, 0 -- для выхода  '))
        elif generation_type == 3:
            try:
                start_generation = int(
                    ord(str(input(f'Задайте символ, {output_words_low}'))))
                end_generation = int(ord(str(input(f'Задайте символ, {output_words_high}'))))
                print('Ваше случайный символ:')
                print(chr(random.randint(start_generation, end_generation)))
                a = int(input('Если хотите дальше генерировать, нажмите что-нибудь, 0 -- для выхода  '))
            except TypeError:
                print('Если хотите получить сгенерированный символ, вводите буквы, символы или цифры (не числа)')
        else:
            print('У нас тут только выбор из трех целых чисел имеется: 1, 2 и 3:)')
    except ValueError:
        print('Введите, пожалуйста, значения из указанных')
