from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        queue = [root]
        ans = []

        while queue:
            node = queue.pop(0)

            if node:
                ans.append(node.val)
                queue = node.children + queue

        return ans