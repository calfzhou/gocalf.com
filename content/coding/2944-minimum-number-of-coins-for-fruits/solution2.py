from collections import deque


class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)
        stack = deque([(0, n)]) # Monotonically increasing stack of (dp(i), i). Use (0, n) as the fence.
        for i in range(n-1, -1, -1):
            # Remove dp(j) where j > 2i + 2.
            r = 2 * i + 2
            while stack[0][1] > r:
                stack.popleft()

            # Now the minimum dp(j) (i+1 <= j <= 2i+2) is stack[0][0].
            cost = prices[i] + stack[0][0]

            # Remove dp(j) where dp(j) >= dp(i).
            while stack and stack[-1][0] >= cost:
                stack.pop()

            # Add dp(i) to the stack.
            stack.append((cost, i))

        return stack[-1][0]
