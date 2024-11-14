import pytest

from node import ListNode
from solution import Solution


@pytest.mark.parametrize('list1, list2, expected', [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
])
class Test:
    def test_solution(self, list1, list2, expected):
        sol = Solution()
        head = sol.mergeTwoLists(self._build_list(list1), self._build_list(list2))
        assert self._format(head) == expected

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

t = Test()
sol = Solution()
sol.mergeTwoLists(t._build_list([1,2,4]), t._build_list([1,3,4]))
