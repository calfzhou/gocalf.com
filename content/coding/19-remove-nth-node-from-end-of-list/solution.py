from typing import Optional

from node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(None, head)
        p1 = p2 = root
        for _ in range(n):
            p2 = p2.next

        while True:
            p2 = p2.next
            if p2 is None:
                break
            p1 = p1.next

        p1.next = p1.next.next

        return root.next
