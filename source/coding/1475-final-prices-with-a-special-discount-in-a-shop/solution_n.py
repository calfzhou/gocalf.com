class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        for i in range(len(prices) - 1, -1, -1):
            p = prices[i]
            while stack and stack[-1] > p:
                stack.pop()

            if stack:
                prices[i] -= stack[-1]

            if not stack or stack[-1] < p:
                stack.append(p)

        return prices
