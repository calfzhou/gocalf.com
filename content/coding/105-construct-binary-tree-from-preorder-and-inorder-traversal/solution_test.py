import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import print_tree
from solution import Solution

null = None


@pytest.mark.parametrize('preorder, inorder, expected', [
    ([3,9,20,15,7], [9,3,15,20,7], [3,9,20,null,null,15,7]),
    ([-1], [-1], [-1]),

    ([3,4,1,6,7,2,0,5], [1,7,6,4,0,2,3,5], [3,4,5,1,2,null,null,null,6,0,null,7]),
])
class Test:
    def test_solution(self, preorder, inorder, expected):
        sol = Solution()
        result = sol.buildTree(preorder, inorder)
        assert print_tree(result) == expected
