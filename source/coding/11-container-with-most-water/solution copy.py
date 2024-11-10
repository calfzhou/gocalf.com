from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        biggest = 0

        # Check each line's left-side max equal-height-container.
        max_height = height[0]
        for i in range(1, n):
            h_i = height[i]
            if max_height < h_i:
                max_height = h_i
                continue

            for j in range(i):
                if height[j] >= h_i:
                    biggest = max(biggest, (i - j) * h_i)
                    break

        # Check each line's right-side max equal-height-container.
        max_height = height[-1]
        for i in range(n - 2, -1, -1):
            h_i = height[i]
            if max_height < h_i:
                max_height = h_i
                continue

            for k in range(n - 1, i, -1):
                if height[k] >= h_i:
                    biggest = max(biggest, (k - i) * h_i)
                    break

        return biggest
