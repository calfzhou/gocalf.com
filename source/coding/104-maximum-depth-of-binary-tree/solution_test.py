import pytest

import sys
sys.path.append('..')
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([3,9,20,null,null,15,7], 3),
    ([1,null,2], 2),
])
class Test:
    def test_solution(self, root, expected):
        sol = Solution()
        assert sol.maxDepth(build_tree(root)) == expected
