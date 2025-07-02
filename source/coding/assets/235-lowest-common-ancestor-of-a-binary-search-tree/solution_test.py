import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import bst_find, build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, p, q, expected', [
    ([6,2,8,0,4,7,9,null,null,3,5], 2, 8, 6),
    ([6,2,8,0,4,7,9,null,null,3,5], 2, 4, 2),
])
class Test:
    def test_solution(self, root, p, q, expected):
        sol = Solution()
        root = build_tree(root)
        p = bst_find(root, p)
        q = bst_find(root, q)
        assert sol.lowestCommonAncestor(root, p, q).val == expected
