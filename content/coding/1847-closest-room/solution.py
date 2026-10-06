class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    @property
    def balance(self) -> int:
        l = self.left.height if self.left else 0
        r = self.right.height if self.right else 0
        return l - r

    @property
    def left_balance(self) -> int:
        return self.left.balance if self.left else 0

    @property
    def right_balance(self) -> int:
        return self.right.balance if self.right else 0

    def re_height(self) -> None:
        l = self.left.height if self.left else 0
        r = self.right.height if self.right else 0
        self.height = 1 + max(l, r)

    def rotate_left(self) -> 'TreeNode':
        right = self.right
        self.right, right.left = right.left, self
        self.re_height()
        right.re_height()
        return right

    def rotate_right(self) -> 'TreeNode':
        left = self.left
        self.left, left.right = left.right, self
        self.re_height()
        left.re_height()
        return left


class AVLTree:
    def __init__(self) -> None:
        self._root: TreeNode = None

    def insert(self, val: int) -> None:
        if self._root is None:
            self._root = TreeNode(val)
            return

        ancestors = []
        node = self._root
        while True:
            ancestors.append(node)
            if val < node.val:
                if node.left is None:
                    node.left = child = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = child = TreeNode(val)
                    break
                else:
                    node = node.right

        while ancestors:
            node = ancestors.pop()
            if child.val < node.val:
                node.left = child
            else:
                node.right = child
            node.re_height()
            balance = node.balance # left height - right height
            if balance > 1:
                if node.left and node.left.balance < 0: # Left-Right
                    node.left = node.left.rotate_left()
                node = node.rotate_right() # Left-Left & Left-Right
            elif balance < -1:
                if node.right and node.right.balance > 0: # Right-Left
                    node.right = node.right.rotate_right()
                node = node.rotate_left() # # Right-Right & Right-Left
            child = node

        self._root = child

    def find(self, val: int) -> tuple[int, int, int]:
        """Finds `val`. If not found, return the largest value < val, and the smallest value > val."""
        lt = gt = None
        node = self._root
        while node:
            if node.val == val:
                return val, None, None
            elif node.val > val:
                gt = node.val
                node = node.left
            else:
                lt = node.val
                node = node.right

        return None, lt, gt


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        k = len(queries)
        queries = [(q[0], q[1], j) for j, q in enumerate(queries)]
        queries.sort(key=lambda q: q[1], reverse=True)
        answer = [-1] * k

        n = len(rooms)
        rooms.sort(key=lambda r: r[1], reverse=True)
        valid_rooms = AVLTree()

        i = 0
        for preferred, min_size, j in queries:
            while i < n and rooms[i][1] >= min_size:
                valid_rooms.insert(rooms[i][0])
                i += 1

            ans, lt, gt = valid_rooms.find(preferred)
            if ans is None:
                ans = lt
                if gt is not None and (ans is None or gt - preferred < preferred - ans):
                    ans = gt

            if ans is not None: answer[j] = ans

        return answer
