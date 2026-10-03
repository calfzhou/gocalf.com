import pytest

from node import ListNode
from solution import Solution


def build_linked_list(values, pos):
    tail = None
    root = ListNode(0) # root's next points to the real head.
    node = root
    for i, val in enumerate(values):
        node.next = node = ListNode(val)
        if pos == i:
            tail = node

    node.next = tail
    return root.next


@pytest.mark.parametrize('values, pos, expected', [
    ([3,2,0,-4], 1, True),
    ([1,2], 0, True),
    ([1], -1, False),
])
class Test:
    def test_solution(self, values, pos, expected):
        head = build_linked_list(values, pos)
        sol = Solution()
        assert sol.hasCycle(head) == expected
