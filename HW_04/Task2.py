# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# python -m timeit -n 100 -s "import Task2" "get_prime_number_1(10)" - для профилирования
import math


# C использованием решета Эратосфена
def get_prime_number_1(place):
    def sieve_of_eratosthenes(max_prime_number):
        # формируем массив с правдами, решето, которое пока пропускает все
        sieve = [True for _ in range(max_prime_number + 1)]
        # убираем 1 и 0, они не являются простыми числами
        sieve[0:1] = [False, False]
        # перебираем числа:
        for start in range(2, max_prime_number + 1):
            # смотрим на место числа в решете
            if sieve[start]:
                # вычеркиваем числа из решета с шагом в это число (c шагом в start)
                for i in range(2 * start, max_prime_number + 1, start):
                    sieve[i] = False
        primes = []
        # формируем массив простых чисел
        for i in range(2, max_prime_number + 1):
            if sieve[i]:
                primes.append(i)
        return primes

    # в массиве простых индекс меньше места числа на 1, так как место простого числа считается с первого
    index = place - 1
    limit_prime_number = place * place
    prime_number = sieve_of_eratosthenes(limit_prime_number)[index]
    return prime_number


# C использованием решета Аткина, без предпросеивания
# Пусть n — натуральное число, которое не делится ни на какой полный квадрат. Тогда:
# 1. если n представимо в виде 4*k+1, то оно просто тогда и только тогда,
# когда число натуральных решений уравнения 4*x**2+y**2 = n нечетно.
# 2. если n представимо в виде 6*k+1, то оно просто тогда и только тогда,
# когда число натуральных решений уравнения 3*x**2+y**2 = n нечетно.
# 3. если n представимо в виде 12*k-1, то оно просто тогда и только тогда,
# когда число натуральных решений уравнения 3*x**2−y**2 = n, для которых x > y, нечетно.

def get_prime_number_2(place):
    def sieve_of_atkin(max_prime_number):
        # формируем первые члены ряда простых чисел:
        primes = [2, 3]
        # формируем массив с неправдами, решето, которое пока не пропускает ничего
        sieve = [False] * (max_prime_number + 1)
        # Перебираем x и y, последовательно проверяем число на возможность представления в квадратичных формах вида:
        # 4*x**2+y**2, 3*x**2+y**2, 3*x**2−y**2:
        for x in range(1, int(math.sqrt(max_prime_number)) + 1):
            for y in range(1, int(math.sqrt(max_prime_number)) + 1):
                n = 4 * x ** 2 + y ** 2
                # проверяем возможность представления n в виде 4*k+1
                if n <= max_prime_number and (n % 12 == 1 or n % 12 == 5):
                    # если
                    sieve[n] = not sieve[n]
                n = 3 * x ** 2 + y ** 2
                # проверяем возможность представления n в виде 6*k+1
                if n <= max_prime_number and n % 12 == 7:
                    sieve[n] = not sieve[n]
                n = 3 * x ** 2 - y ** 2
                # проверяем возможность представления n в виде 12*k-1
                if x > y and n <= max_prime_number and n % 12 == 11:
                    sieve[n] = not sieve[n]
        # Первые два члена ряда простых числа уже есть, 2 и 3, поэтому начинаем счет с 5:
        for x in range(5, int(math.sqrt(max_prime_number))):
            if sieve[x]:
                #  Вычеркиваем квадраты простых чисел:
                for y in range(x ** 2, max_prime_number + 1, x ** 2):
                    sieve[y] = False
        # Формируем массив простых чисел:
        for prime in range(5, max_prime_number):
            if sieve[prime]:
                primes.append(prime)
        return primes

    index = place - 1
    limit_prime_number = place * place
    prime_number = sieve_of_atkin(limit_prime_number)[index]
    return prime_number


# Проверка на одинаковорабочесть:
# print(get_prime_number_1(100))
# print(get_prime_number_2(100))
