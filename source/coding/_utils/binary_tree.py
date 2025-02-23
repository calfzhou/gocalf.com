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


def bst_find(root: TreeNode | None, value: int) -> TreeNode | None:
    while root and root.val != value:
        root = root.left if value < root.val else root.right

    return root


def traverse_tree(root: TreeNode | None) -> tuple[list[int], list[int], list[int]]:
    preorder = []
    inorder = []
    postorder = []
    stack = []
    prev = None
    while root or stack:
        if root:
            preorder.append(root.val)
            stack.append(root)
            root = root.left
        elif stack[-1].right != prev:
            inorder.append(stack[-1].val)
            root = stack[-1].right
            prev = None
        else:
            if prev is None:
                inorder.append(stack[-1].val)
            prev = stack.pop()
            postorder.append(prev.val)

    return preorder, inorder, postorder
