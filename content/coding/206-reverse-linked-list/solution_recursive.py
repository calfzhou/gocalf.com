from typing import Optional

from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        return self._helper(head)

    def _helper(self, head: ListNode) -> ListNode:
        if (next := head.next) is None:
            return head

        first = self._helper(next)
        next.next = head
        head.next = None
        return first
