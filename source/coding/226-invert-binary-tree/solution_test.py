import pytest

import sys
sys.path.insert(0, '..')
from _utils.binary_tree import build_tree, print_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
    ([], []),
])
class Test:
    def test_solution(self, root, expected):
        sol = Solution()
        result = sol.invertTree(build_tree(root))
        assert print_tree(result) == expected
