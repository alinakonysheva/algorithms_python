# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
first_place = 32
last_place = 127

for i in range(first_place, last_place):

    if i % 10 == first_place % 10:
        print(f'{chr(i)}  ')
    else:
        print(f'{chr(i)}  ', end='')
