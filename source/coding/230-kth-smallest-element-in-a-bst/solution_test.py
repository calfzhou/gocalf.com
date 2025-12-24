import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, k, expected', [
    ([3,1,4,null,2], 1, 1),
    ([5,3,6,2,4,null,null,1], 3, 3),
])
class Test:
    def test_solution(self, root, k, expected):
        sol = Solution()
        assert sol.kthSmallest(build_tree(root), k) == expected
