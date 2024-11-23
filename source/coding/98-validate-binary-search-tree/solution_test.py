import pytest

import sys
sys.path.insert(0, '..')
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([2,1,3], True),
    ([5,1,4,null,null,3,6], False),

    ([2,2,2], False),
    ([5,4,6,null,null,3,7], False),
])
class Test:
    def test_solution(self, root, expected):
        sol = Solution()
        assert sol.isValidBST(build_tree(root)) == expected
