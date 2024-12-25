import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution

null = None


@pytest.mark.parametrize('root, expected', [
    ([1,3,2,5,3,null,9], [1,3,9]),
    ([1,2,3], [1,3]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, root, expected):
    assert sol.largestValues(build_tree(root)) == expected
