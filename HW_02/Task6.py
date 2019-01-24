# 6. В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или
# меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.
import random


lucky_number = random.randint(0, 100)
attempts = 10
print("Загадано целое число от 0 до 100. Попробуйте его угадать!")
print("Вам дается 10 попыток и подсказки (больше или меньше загаданного введенное Вами число)")

for i in range(1, attempts):
    user_number = int(input(f'Попытка номер {i}, какое Ваше целочисленное предположение? --> '))
    if user_number < lucky_number:
        print(f'{user_number} меньше загаданного! Попробуйте еще раз!')
    elif user_number > lucky_number:
        print(f'{user_number} больше загаданного! Попробуйте еще раз!')
    else:
        print(f'{user_number} равно загаданному числу! Ура!')
        break
else:
    print(f'Сегодня не Ваш день, загаданное число -- {lucky_number}')


