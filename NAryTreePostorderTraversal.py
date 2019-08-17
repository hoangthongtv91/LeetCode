from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if root:
            if root.children:
                for child in root.children:
                    ans += self.postorder(child)
            ans += [root.val]
        return ans