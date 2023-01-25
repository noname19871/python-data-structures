from linked_list import SingleLinkedList
from linked_list.linked_list import Node


def cmp(a, b):
    if a < b:
        return 1
    if a == b:
        return 0
    return -1


tmp = SingleLinkedList(data=[1, 5, 3, 2, 10])
gjg = Node(1, Node(2, Node(10)))
tmp2 = SingleLinkedList(head=gjg, data=[1, 3, 2])

print(len(tmp2))
tmp.sort(cmp=cmp)
print(tmp)
print(tmp2)
