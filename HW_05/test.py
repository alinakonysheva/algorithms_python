# подаем на вход перевернутые числа
a = [1, 5, 11]
b = [1, 5]
product = [0 * i for i in range(len(a) + len(b))]

a.reverse()
b.reverse()

for i, element1 in enumerate(a):
    for j, element2 in enumerate(b):
        product[i + j] = product[i + j] + element1 * element2

for i, element in enumerate(product):
    if element >= 15:
        product[i + 1] = product[i + 1] + element // 16
        product[i] = element % 16

product.reverse()
result = ' '.join(str(e) for e in product).lstrip('0') or '0'
print(f' После приведения к шестнадцатиричной системе {result}')
