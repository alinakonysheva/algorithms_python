# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# пишем функцию, которая будет искать сумму цифр произвольного числа


def numerals_summ(number):
    summ = 0
    while number > 0:
        # вытаскиваем цифры из числа:
        number_without_last = int(number/10)
        last_numeral = number - 10 * number_without_last
        summ = summ + last_numeral
        number = number_without_last
    return summ


usernum = 1
max_user_sum = 0
max_user_num = 0
# пока пользователь не введет 0, считаем сумму всех цифр и ищим среди всех чисел максимальную сумму цифр
while usernum != 0:
    usernum = int(input("Введите, пожалуйста, натуральное число:   "))
    user_sum = numerals_summ(usernum)
    # ищем максимальную сумму и сохраняем в переменной max_user_sum,
    # отмечаем число max_user_num в котором искали сумму
    if user_sum > max_user_sum:
        max_user_sum = user_sum
        max_user_num = usernum

print(max_user_num, max_user_sum)
