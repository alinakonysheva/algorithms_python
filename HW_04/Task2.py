# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# python -m timeit -n 100 -s "import Task2" "Task2.rec_fib(10)" - для профилирования
# C использованием решета Эратосфена
def get_prime_number_1(place):
    def sieve_of_eratosthenes(max_prime_number):
        # формируем массив с правдами
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
# проверка для простого числа 13:
# print(get_prime_number_1(6))


"""
def rec_fib(n):
    if n < 2:
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


# 100 loops, best of 5: 34 usec per loop - при n = 10
# ... сделать несколько замеров

def test_rec_fib(func):
    fibonacci_series = [0, 1, 1, 2, 3, 5, 8, 13]
    for i, item in enumerate(fibonacci_series):
        assert item == func(i)
        print(f'Test {i} is ok')
"""
