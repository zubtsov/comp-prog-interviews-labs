# https://leetcode.com/problems/symmetric-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeValueIterator:
    def __init__(self, tree_node: Optional[TreeNode], left_first=True):
        self.__left_first = left_first
        self.__tree_node = tree_node

    def __iter__(self):
        return self.__node_value_generator(self.__tree_node)

    def __node_value_generator(self, tn: Optional[TreeNode]):
        if tn is None:
            yield None
        else:
            yield tn.val

            if self.__left_first:
                yield from self.__node_value_generator(tn.left)
                yield from self.__node_value_generator(tn.right)
            else:
                yield from self.__node_value_generator(tn.right)
                yield from self.__node_value_generator(tn.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        no_nodes = not root
        only_one_node = not root.left and not root.right

        if no_nodes or only_one_node:
            return True

        bfi1 = list(TreeNodeValueIterator(root.left, left_first=True))
        bfi2 = list(TreeNodeValueIterator(root.right, left_first=False))

        return all(map(lambda t: t[0] == t[1], zip(bfi1, bfi2)))


### Test only
def array_to_binary_tree(array_of_node_values):
    if len(array_of_node_values) == 0:
        return None

    tree_nodes = [
        TreeNode(val) if val is not None else None for val in array_of_node_values
    ]

    for i in range(len(array_of_node_values)):
        tni = tree_nodes[i]
        if tni:
            left_child_index = 2 * i + 1
            if left_child_index < len(array_of_node_values):
                tni.left = tree_nodes[left_child_index]

            right_child_index = 2 * i + 2
            if right_child_index < len(array_of_node_values):
                tni.right = tree_nodes[right_child_index]

    return tree_nodes[0]


if __name__ == "__main__":
    root = array_to_binary_tree([1, 2, 2, None, 3, None, 3])
    print(Solution().isSymmetric(root))
