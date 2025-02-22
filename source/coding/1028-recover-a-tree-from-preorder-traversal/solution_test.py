import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import print_tree
from solution import Solution

null = None


@pytest.mark.parametrize('traversal, expected', [
    ("1-2--3--4-5--6--7", [1,2,5,3,4,6,7]),
    ("1-2--3---4-5--6---7", [1,2,5,3,null,6,null,4,null,7]),
    ("1-401--349---90--88", [1,401,null,349,88,90]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, traversal, expected):
    root = sol.recoverFromPreorder(traversal)
    res = print_tree(root)
    assert res == expected
