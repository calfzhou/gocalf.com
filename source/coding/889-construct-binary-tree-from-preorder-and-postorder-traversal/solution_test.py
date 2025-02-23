import pytest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from _utils.binary_tree import TreeNode, print_tree, traverse_tree
from solution import Solution

null = None


def verify(root: TreeNode | None, preorder_exp: list[int], postorder_exp: list[int]) -> None:
    preorder, _, postorder = traverse_tree(root)
    assert preorder == preorder_exp
    assert postorder == postorder_exp


@pytest.mark.parametrize('preorder, postorder, expected', [
    ([1,2,4,5,3,6,7], [4,5,2,6,7,3,1], [1,2,3,4,5,6,7]),
    ([1], [1], [1]),

    ([3,4,1,6,7,2,8,5], [7,6,1,8,2,4,5,3], [3,4,5,1,2,null,null,null,6,0,null,7]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, preorder, postorder, expected):
    root = sol.constructFromPrePost(preorder, postorder)
    if print_tree(root) != expected:
        verify(root, preorder, postorder)
