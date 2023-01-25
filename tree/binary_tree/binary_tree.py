from typing import Any, List, Optional

from tree.binary_tree.node import Node


def traverse(cur_node: Optional[Node], traversal_type: str = 'inorder') -> List[Any]:
    """
    O(n) time complexity
    O(h) space complexity (because of recursion and system stack usage),
    O(1) space complexity if we don't consider the size of the system stack

    DFS-like approach
    """
    if not cur_node:
        return []

    if traversal_type == 'preorder':
        return [cur_node.data] + traverse(cur_node.left, traversal_type) + traverse(cur_node.right, traversal_type)
    elif traversal_type == 'postorder':
        return traverse(cur_node.left, traversal_type) + traverse(cur_node.right, traversal_type) + [cur_node.data]
    else:
        traverse(cur_node.left, traversal_type) + [cur_node.data] + traverse(cur_node.right, traversal_type)


def inorder_traverse_with_stack(cur_node: Optional[Node]) -> List[Any]:
    """
    O(n) time complexity
    O(h) space complexity (max stack size == max tree height)

    DFS-like approach
    """
    if not cur_node:
        return []

    res = []
    stack = []
    while True:
        if cur_node.left:
            stack.append(cur_node)
            cur_node = cur_node.left
        elif stack:
            res.append(cur_node.data)
            cur_node = cur_node.right
        else:
            break
    return res


def level_traversal(cur_node: Optional[Node]) -> List[Any]:
    pass


class BinaryTree:
    def __init__(self, root: Optional[Node]):
        self.root = root

    def build_complete_binary_tree(self, data: List[Any]):
        """
        Complete binary tree is the tree where all the levels are completely filled except possibly the last level and
        the last level has all keys as left as possible

        O(n) time complexity
        """

        if not data:
            self.root = None

        self.root = Node(data=data[0])
        stack = [self.root]

        while stack:
            cur_node = stack.pop(0)


