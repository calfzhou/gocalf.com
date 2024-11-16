import collections

import pytest

from solution import Codec
from utils import TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    virtual = TreeNode(None)
    queue = collections.deque()
    queue.append((virtual, 'left'))
    for val in values:
        node, branch = queue.popleft()
        if val is None:
            continue

        child = TreeNode(val)
        setattr(node, branch, child)
        queue.append((child, 'left'))
        queue.append((child, 'right'))

    return virtual.left


def trees_equal(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    if root1 == root2:
        return True

    if root1.val != root2.val:
        return False

    return trees_equal(root1.left, root2.left) and trees_equal(root1.right, root2.right)


@pytest.mark.parametrize('values', [
    ([1,2,3,None,None,4,5]),
    ([]),

    ([1,2,3]),
    ([1,None,2,3]),
    ([5,4,7,3,None,2,None,-1,None,9]),
])
class Test:
    def test_solution(self, values):
        ser = Codec()
        deser = Codec()
        root = build_tree(values)
        data = ser.serialize(root)
        new_root = deser.deserialize(data)
        assert trees_equal(root, new_root)
        assert data == ser.serialize(new_root)
