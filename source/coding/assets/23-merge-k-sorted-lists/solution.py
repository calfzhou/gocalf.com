from typing import List, Optional

from node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class MinHeapMerger:
    def __init__(self, heads) -> None:
        self.store = list(filter(None, heads))
        self._build()

    def size(self):
        return len(self.store)

    def pop(self):
        root = self.store[0]
        if root.next is not None:
            self.store[0] = root.next
        elif len(self.store) > 1:
            self.store[0] = self.store.pop()
        else:
            return self.store.pop()

        self._shift_down(0)
        return root

    def _build(self):
        leaf = len(self.store) >> 1
        for i in range(leaf - 1, -1, -1):
            self._shift_down(i)

    def _shift_up(self, pos: int):
        """Shifts store[pos] up to proper new position."""
        while pos > 0:
            parent = (pos - 1) >> 1
            if self.store[parent].val > self.store[pos].val:
                self.store[parent], self.store[pos] = self.store[pos], self.store[parent]
                pos = parent
            else:
                return

    def _shift_down(self, pos: int):
        """Shifts store[pos] down to proper new position."""
        n = len(self.store)
        leaf = n >> 1
        while pos < leaf:
            left = (pos << 1) + 1
            right = left + 1
            child = right if right < n and self.store[right].val < self.store[left].val else left
            if self.store[pos].val > self.store[child].val:
                self.store[pos], self.store[child] = self.store[child], self.store[pos]
                pos = child
            else:
                return


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = node = ListNode()
        merger = MinHeapMerger(lists)
        while merger.size() > 0:
            node.next = node = merger.pop()
        return root.next
