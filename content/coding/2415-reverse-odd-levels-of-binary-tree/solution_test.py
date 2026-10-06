import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree, print_tree
from solution import Solution


@pytest.mark.parametrize('root, expected', [
    ([2,3,5,8,13,21,34], [2,5,3,8,13,21,34]),
    ([7,13,11], [7,11,13]),
    ([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2], [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, root, expected):
    result = sol.reverseOddLevels(build_tree(root))
    assert print_tree(result) == expected
