from random import randrange
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional['ListNode']):
        self._head = head
        self._n = 0
        while head:
            self._n += 1
            head = head.next

    def getRandom(self) -> int:
        node = self._head
        choose = randrange(self._n)
        for _ in range(choose):
            node = node.next

        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
