from typing import Any, Callable, List, Optional

from linked_list.linked_list import Node

from linked_list.utils import get_length, merge_sort


class SingleLinkedList:
    def __init__(self, head: Optional[Node] = None, data: Optional[List[Any]] = None):
        """
        O(n) time, O(1) space
        """

        self.head = head
        self._length = 0
        if self.head is not None:
            self._length = get_length(self.head)

        if data is not None:
            self._length += len(data)
            if not self.head:
                self.head = Node()

            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next

            for val in data:
                new_node = Node(val)
                cur_node.next = new_node
                cur_node = cur_node.next

            if not self.head.val:
                self.head = self.head.next

    def __len__(self):
        return self._length

    def __str__(self):
        """
        O(n) time, O(1) space
        """
        cur_node = self.head
        string_representation = ""
        while cur_node:
            string_representation += str(cur_node.val)
            if cur_node.next:
                string_representation += " "
            cur_node = cur_node.next
        return string_representation

    def sort(self, cmp: Optional[Callable] = None, reverse: bool = False) -> None:
        """
        Bottom-up Merge Sort without recursion
        O(n log n) time, O(1) space since we use constant number of variables to store
        """
        new_head = merge_sort(self.head, self._length, cmp, reverse)
        self.head = new_head
