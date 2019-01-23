numbers_into_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def move_to_hexadecimal(list1):
    list_hex = list1.copy()
    for i, element in enumerate(list1):
        if element > 9:
            list_hex.insert(i, numbers_into_letters[element])
            del list_hex[i + 1]
    return list_hex

print(move_to_hexadecimal([12, 14, 0, 15, 10]))