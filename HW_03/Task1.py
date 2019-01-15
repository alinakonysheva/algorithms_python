# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# Заводим счетчики для цифр от 2 до 9

int_2 = 0
int_3 = 0
int_4 = 0
int_5 = 0
int_6 = 0
int_7 = 0
int_8 = 0
int_9 = 0

# перебираем натуральные числа от 2 до 99:
for i in range(2, 100):
    # ищем кратные двум, двумя и четырем, двум, четырем и восьми:
    if i % 2 == 0:
        int_2 = int_2 + 1
        if i % 4 == 0:
            int_4 = int_4 + 1
            if i % 8 == 0:
                int_8 = int_8 + 1
    # ищем кратные трем, трем и шести, трем и девяти:
    if i % 3 == 0:
        int_3 = int_3 + 1
        if i % 6 == 0:
            int_6 = int_6 + 1
        if i % 9 == 0:
            int_9 = int_9 + 1
    # ищем кратные 7:
    if i % 7 == 0:
        int_7 = int_7 + 1
    # ищем кратные 5:
    if i % 5 == 0:
        int_5 = int_5 + 1

print("Количество чисел в диапазоне от 2 до 99, которые кратны  ")
print(f"двум равно: {int_2}")
print(f"трем равно: {int_3}")
print(f"четырем равно: {int_4}")
print(f"пяти равно: {int_5}")
print(f"шести равно: {int_6}")
print(f"семи равно: {int_7}")
print(f"восьми равно: {int_8}")
print(f"девяти равно: {int_9}")

# или:
start_num = 2
last_num = 99
start_div = 2
end_div = 9
for i in range(start_div, end_div + 1):
    freq = 0
    for j in range(start_num, last_num + 1):
        if j % i == 0:
            freq += 1
    print(f' Числу {i} кратно {freq} чисел')
