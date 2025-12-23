import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3

null = None


@pytest.mark.parametrize('root, expected', [
    ([3,2,3,null,3,null,1], 7),
    ([3,4,5,1,3,null,1], 9),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2(), Solution3()])
class Test:
    def test_solution(self, sol, root, expected):
        assert sol.rob(build_tree(root)) == expected
