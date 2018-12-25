#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input("Введите, пожалуйста, натуральное число   "))
# заводим место под перевернутый номер
reverse_number = 0

while number > 0:
    number_without_last = int(number/10)
    last_numeral = number - 10 * number_without_last
# переворачиваем число
    reverse_number = reverse_number*10 + last_numeral
    number = number_without_last

print(reverse_number)
