import pytest

from solution import Solution
from solution_recursive import Solution as SolutionRecursive
from utils import build_linked_list, format_linked_list

@pytest.mark.parametrize('head, expected', [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], []),
])
class Test:
    def test_solution(self, head, expected):
        sol = Solution()
        result = sol.reverseList(build_linked_list(head))
        assert format_linked_list(result) == expected

    def test_solution_recursive(self, head, expected):
        sol = SolutionRecursive()
        result = sol.reverseList(build_linked_list(head))
        assert format_linked_list(result) == expected
