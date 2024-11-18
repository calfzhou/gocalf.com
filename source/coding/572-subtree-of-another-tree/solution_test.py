import pytest

from solution import Solution
from utils import build_tree, TreeNode

null = None


@pytest.mark.parametrize('root, subRoot, expected', [
    ([3,4,5,1,2], [4,1,2], True),
    ([3,4,5,1,2,null,null,null,null,0], [4,1,2], False),
])
class Test:
    def test_solution(self, root, subRoot, expected):
        sol = Solution()
        root = build_tree(root)
        subRoot = build_tree(subRoot)
        assert sol.isSubtree(root, subRoot) == expected
