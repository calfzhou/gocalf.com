import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import print_tree
from solution import Solution
from solution2 import Solution as Solution2

null = None


@pytest.mark.parametrize('n, expected', [
    (3, [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]),
    (1, [[1]]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, n, expected):
    result = sol.generateTrees(n)
    result = [print_tree(root) for root in result]
    result.sort()
    assert result == sorted(expected)
