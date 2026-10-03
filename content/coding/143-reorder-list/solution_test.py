import pytest

from node import ListNode
from solution import Solution


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4], [1,4,2,3]),
    ([1,2,3,4,5], [1,5,2,4,3]),
])
class Test:
    def test_solution(self, values, expected):
        sol = Solution()
        head = self._build_list(values)
        sol.reorderList(head)
        result = self._format(head)
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
