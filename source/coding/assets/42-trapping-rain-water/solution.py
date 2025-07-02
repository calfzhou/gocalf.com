class Solution:
    def trap(self, height: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        min2 = lambda a, b: a if a <= b else b

        n = len(height)
        r_maxes = [0] * n
        r_maxes[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            r_maxes[i] = max2(r_maxes[i + 1], height[i])

        total = 0
        l_max = height[0]
        for i in range(1, n - 1):
            l_max = max2(l_max, height[i])
            bound = min2(l_max, r_maxes[i])
            if bound > height[i]:
                total += bound - height[i]

        return total
