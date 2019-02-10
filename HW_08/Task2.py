# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import collections
import operator

decoded_string = 'Liberte, Egalite, Fraternite'
print(f'Исходная строка: {decoded_string}')
value_weight = collections.Counter(decoded_string)
sorted_value_weight = []
# преобразуем строку в словарь из кортежей символ-вес
sorted_value_weight = sorted(value_weight.items(), key=operator.itemgetter(1))


# созданем класс узла дерева:

class MyNode:
    def __init__(self, value, freq, left=None, right=None):
        self.freq = freq
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_freq(self):
        return self.freq

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def __repr__(self):
        return f'MyNode(freq = {self.freq}, value = {self.value}, left = {self.left}, right = {self.right})'


# преобразуем все элементы словаря в узлы:
nodes = collections.deque([])
for i in range(len(sorted_value_weight)):
    nodes.append(MyNode(sorted_value_weight[i][0], sorted_value_weight[i][1]))


# сворачиваем два узла в один:
def pack(node_1, node_2):
    left = node_1 if node_1.get_freq() <= node_2.get_freq() else node_2
    right = node_2 if node_1.get_freq() <= node_2.get_freq() else node_1
    return MyNode(None, freq=node_1.get_freq() + node_2.get_freq(), left=left, right=right)


# сортируем узлы по возрастанию частоты вхождения:
def reorder(nods):
    return collections.deque(sorted(nods, key=lambda x: x.get_freq()))


# сворачиваем список узлов в дерево:
while len(nodes) > 1:
    node1 = nodes.popleft()
    node2 = nodes.popleft()
    node = pack(node1, node2)
    nodes.appendleft(node)
    nodes = reorder(nodes)


# проходим по дереву узлов, рекурсивно собираем '0', если прошли слева, и '1', если прошли справа
def go_through_tree(my_node, path, elements_codes):
    # для пустого узла возвращаем пустой список
    if my_node is None:
        return []
    # если это лист, то добавляем "код символа"
    elif my_node.is_leaf():
        elements_codes.append((my_node.get_value(), path))
        return elements_codes
    # рассчитываем коды для левой и правой ветвей узла
    else:
        codes_left = go_through_tree(my_node.get_left(), path + '0', [])
        codes_right = go_through_tree(my_node.get_right(), path + '1', [])
        return elements_codes + codes_left + codes_right


encoded_string = []
encode_dictionary = dict(go_through_tree(nodes.pop(), '', []))
print('Закодированная строка: ', end='')
for i in decoded_string:
    encoded_string.append(encode_dictionary[i])
    print(encode_dictionary[i], end=' ')

print()
decode_dictionary = {}
for key, value in encode_dictionary.items():
    decode_dictionary[value] = key

print('Раскодированная строка: ', end='')
for i in encoded_string:
    print(decode_dictionary[i], end='')
