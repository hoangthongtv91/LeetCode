class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        self.res = 0

        def _helper(node):
            if not node:
                return
            if L <= node.val <= R:
                self.res += node.val
            if node.val > L:
                _helper(node.left)
            if node.val < R:
                _helper(node.right)

        _helper(root)

        return self.res