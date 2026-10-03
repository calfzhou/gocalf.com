import pytest

from node import ListNode
from solution import Solution


@pytest.mark.parametrize('values, n, expected', [
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1], 1, []),
    ([1,2], 1, [1]),

    ([1,2,3,4,5], 1, [1,2,3,4]),
    ([1,2,3,4,5], 5, [2,3,4,5]),
])
class Test:
    def test_solution(self, values, n, expected):
        sol = Solution()
        head = self._build_list(values)
        res_head = sol.removeNthFromEnd(head, n)
        result = self._format(res_head)
        assert result == expected

    def _build_list(self, values: list[int]) -> ListNode | None:
        root = ListNode()
        node = root
        for v in values:
            node.next = node = ListNode(v)

        return root.next

    def _format(self, head: ListNode | None) -> list[int]:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        return values
