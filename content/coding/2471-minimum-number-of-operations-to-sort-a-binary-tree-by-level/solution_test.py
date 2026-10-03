import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([1,4,3,7,6,8,5,null,null,null,null,9,null,10], 3),
    ([1,3,2,7,6,5,4], 3),
    ([1,2,3,4,5,6], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, root, expected):
    assert sol.minimumOperations(build_tree(root)) == expected
