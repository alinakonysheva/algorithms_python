# 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

# Делаем две функции для вычисления  1+2+...+n
# делаем рекурсивную функцию, которая будет считать целые числа от i до n (число, который укажет пользователь)


def summ_int(n, i, summ):
    if i <= n:
        summ = summ + i
        i = i + 1
        return summ_int(n, i, summ)
    else:
        return summ - 1

# делаем функцию для вычисления левой части:


def sum_left_part(n):
    return summ_int(n, 1, 1)


# Делаем фукнцию для вычисления правой части:


def sum_right_part(n):
    return int(0.5*n*(n + 1))


print("Давайте проверим справедливость равенства: 1+2+...+n = n(n+1)/2")
n = int(input("Введите, пожалуйста, натуральное число, на котором Вы хотите проверить (до 996)   "))

print(f" Сумма 1+2+...+n, где n = {n} равно {sum_left_part(n)}")
print(f"n(n+1)/2, где n = {n} равно {sum_right_part(n)}")

if sum_left_part(n) == sum_right_part(n):
    print("Чудесно, равенство справедливо!")

else:
    print("Кошмар, равенство несправедливо!")
