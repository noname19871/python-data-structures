from typing import Callable, Optional

from linked_list.linked_list import Node


def get_length(head: Optional[Node]) -> int:
    length = 0
    while head:
        head = head.next
        length += 1
    return length


def merge_sort_split(head: Optional[Node], size: int) -> Optional[Node]:
    # making size - 1 steps until the next chunk found
    for i in range(size - 1):
        if not head:
            break
        head = head.next

    if not head:
        return None

    # find next chunk start and disconnect previous chunk
    next_start, head.next = head.next, None

    return next_start


def merge_sort_merge(left, mid, fake_start, cmp: Optional[Callable] = None, reverse: bool = False):
    # connect nodes from left and mid one by one to our fake_start
    cur_node = fake_start
    while left and mid:
        if (cmp is not None and cmp(left.val, mid.val) <= 0) or (cmp is None and left.val <= mid.val):
            if not reverse:
                cur_node.next, left = left, left.next
            else:
                cur_node.next, mid = mid, mid.next
        else:
            if not reverse:
                cur_node.next, mid = mid, mid.next
            else:
                cur_node.next, left = left, left.next
        cur_node = cur_node.next

    # at the end we have one node left, connect it too
    cur_node.next = left if left else mid

    # move to the end of the new sequence of nodes to establish a fake_start for the next merge
    while cur_node.next:
        cur_node = cur_node.next
    return cur_node


def merge_sort(head: Optional[Node],
               length: Optional[int],
               cmp: Optional[Callable] = None,
               reverse: bool = False) -> Optional[Node]:
    """
    Bottom-up Merge Sort without recursion
    O(n log n) time, O(1) space since we use constant number of variables to store
    """
    if not head or not head.next:
        return head

    fake_head = Node()
    fake_head.next = head
    next_sublist, fake_start, size = None, None, 1
    if not length:
        head_length = get_length(head)
    else:
        head_length = length

    while size < head_length:
        fake_start = fake_head
        next_sublist = fake_start.next
        while next_sublist:
            left = next_sublist
            mid = merge_sort_split(left, size)  # found sublist to be merged
            next_sublist = merge_sort_split(mid, size)  # found next sublist to work in next iter
            # merged two sub lists to the fake start and return new fake start for the next sub lists
            fake_start = merge_sort_merge(left, mid, fake_start, cmp, reverse)  # returned tail = next dummy_start
        size *= 2
    return fake_head.next
