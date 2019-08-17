class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        while head:
            head = head.next
            count += 1

        for i in range(count // 2):
            head = head.next

        return head