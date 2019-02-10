# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import collections
import operator

decoded_string = 'Liberte, Egalite, Fraternite'
value_weight = collections.Counter(decoded_string)
sorted_value_weight = []
sorted_value_weight = sorted(value_weight.items(), key=operator.itemgetter(1))


# создание узла дерева:

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


nods = collections.deque([])
for i in range(len(sorted_value_weight)):
    nods.append(MyNode(sorted_value_weight[i][0], sorted_value_weight[i][1]))


def pack(node_1, node_2):
    left = node_1 if node_1.get_freq() <= node_2.get_freq() else node_2
    right = node_2 if node_1.get_freq() <= node_2.get_freq() else node_1
    return MyNode(None, freq=node_1.get_freq() + node_2.get_freq(), left=left, right=right)


def reorder(nodes):
    return collections.deque(sorted(nodes, key=lambda x: x.get_freq()))


while len(nods) > 1:
    node1 = nods.popleft()
    node2 = nods.popleft()
    node = pack(node1, node2)
    nods.appendleft(node)
    nods = reorder(nods)


def go_through_tree(node, code, elemnts_codes):
    if node is None:
        return []
    elif node.is_leaf():
        elemnts_codes.append((node.get_value(), code))
        return elemnts_codes
    else:
        ltree = go_through_tree(node.get_left(), code + '0', [])
        rtree = go_through_tree(node.get_right(), code + '1', [])
        return elemnts_codes + ltree + rtree


lst = go_through_tree(nods.pop(), '', [])
encoded_string = []
encode_dictionary = dict(lst)
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
