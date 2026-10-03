from typing import Optional

from node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the start node of the right part (to be inverted).
        p1 = p2 = head
        while p2 is not None:
            p2 = p2.next
            if p2 is None:
                break
            p1 = p1.next
            p2 = p2.next

        right, p1.next = p1.next, None

        # Invert the right half list.
        prev = None
        curr = right
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next

        right = prev

        # Merge left half and inverted right half into one.
        while right is not None:
            head.next, right.next, head, right = right, head.next, head.next, right.next
