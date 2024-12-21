import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([1,null,2,3], [3,2,1]),
    ([1,2,3,4,5,null,8,null,null,6,7,9], [4,6,7,5,2,9,8,3,1]),
    ([], []),
    ([1], [1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, root, expected):
    assert sol.postorderTraversal(build_tree(root)) == expected
