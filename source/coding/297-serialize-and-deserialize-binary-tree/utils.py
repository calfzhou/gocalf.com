class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        left = str(self.left.val) if self.left else 'X'
        right = str(self.right.val) if self.right else 'X'
        return f'{left} <- {self.val} -> {right}'
