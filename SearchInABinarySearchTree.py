class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        currentNode = root
        while currentNode:
            if currentNode.val == val:
                return currentNode
            elif val > currentNode.val:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        return currentNode