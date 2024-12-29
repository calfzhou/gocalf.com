import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import build_tree
from _utils.linked_list import build_linked_list
from solution import Solution

null = None


@pytest.mark.parametrize('head, root, expected', [
    ([4,2,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3], True),
    ([1,4,2,6], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3], True),
    ([1,4,2,6,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3], False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, head, root, expected):
    assert sol.isSubPath(build_linked_list(head), build_tree(root)) == expected
