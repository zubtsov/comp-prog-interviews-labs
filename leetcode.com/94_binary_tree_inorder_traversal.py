from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TODO: implement a non-recursive iterative solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]

        if root.left:
            res[0:0] = self.inorderTraversal(root.left)
        if root.right:
            res[len(res):] = self.inorderTraversal(root.right)

        return res
