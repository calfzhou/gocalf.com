import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([3,9,20,null,null,15,7], [[3],[9,20],[15,7]]),
    ([1], [[1]]),
    ([], []),
])
class Test:
    def test_solution(self, root, expected):
        sol = Solution()
        assert sol.levelOrder(build_tree(root)) == expected
