import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('p, q, expected', [
    ([1,2,3], [1,2,3], True),
    ([1,2], [1,null,2], False),
    ([1,2,1], [1,1,2], False),
])
class Test:
    def test_solution(self, p, q, expected):
        sol = Solution()
        assert sol.isSameTree(build_tree(p), build_tree(q)) == expected
