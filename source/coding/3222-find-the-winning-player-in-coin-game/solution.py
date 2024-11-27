class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        n = y >> 2
        if x < n:
            n = x

        return 'Alice' if n & 1 else 'Bob'
