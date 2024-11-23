import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        left = str(self.left.val) if self.left else 'X'
        right = str(self.right.val) if self.right else 'X'
        return f'{left} <- {self.val} -> {right}'


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


def print_tree(root: TreeNode | None) -> list[int | None]:
    values = []
    queue = collections.deque()
    queue.append(root)
    while len(queue) > 0:
        root = queue.popleft()
        if root is None:
            values.append(None)
        else:
            values.append(root.val)
            queue.append(root.left)
            queue.append(root.right)

    while values and values[-1] is None:
        values.pop()
    return values
