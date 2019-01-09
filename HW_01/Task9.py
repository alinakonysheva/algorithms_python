# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

output_words = 'Введите, пожалуйста, '
number1 = float(input(f'{output_words} первое число --> '))
number2 = float(input(f'{output_words} второе число --> '))
number3 = float(input(f'{output_words} третье число --> '))

if number1 > number2:
    if number2 > number3:
        print(f'{number2} -- среднее')

    else:
        if number3 > number1:
            print(f'{number1} -- среднее')
        else:
            print(f'{number3} -- среднее')
else:
    if number2 > number3:
        if number3 > number1:
            print(f'{number3} -- среднее')
        else:
            print(f'{number1} -- среднее')
    else:
        print(f'{number2} -- среднее')
