import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.linked_list import build_linked_list, format_linked_list
from solution import Solution


@pytest.mark.parametrize('l1, l2, expected', [
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
])
class Test:
    def test_solution(self, l1, l2, expected):
        sol = Solution()
        res = sol.addTwoNumbers(build_linked_list(l1), build_linked_list(l2))
        assert format_linked_list(res) == expected
