# 4. Определить, какое число в массиве встречается чаще всего.

list_init = [0, 3, 0, 0, 0, 5, 6, -6, 4, 5, 13, 9, 56, 24, -10, 5, 5, 5, 0, 0]

counter_elements = {}
max_count = 0
max_item = None

for i in list_init:
    if i in counter_elements:
        counter_elements[i] = counter_elements[i] + 1
    else:
        counter_elements[i] = 1

    if counter_elements[i] > max_count:
        max_count = counter_elements[i]
        max_item = i

print(f"Самый часто встречающийся элемент в массиве это {max_item}, который встречается {max_count} раз/раза")

