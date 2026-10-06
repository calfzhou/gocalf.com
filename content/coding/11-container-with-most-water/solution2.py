from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        edges = [0, len(height) - 1] # Current container's left and right edge index.
        moving = 0 # 0: moving left edge; 1: moving right edge.
        h = 0 # Current container's height.
        h_fixed = 0 # The not-moving edge's height.
        steps = (1, -1)
        max_area = 0
        while edges[0] < edges[1]:
            if (h_moving := height[edges[moving]]) <= h:
                edges[moving] += steps[moving]
                continue

            if h_moving > h_fixed:
                h, h_fixed = h_fixed, h_moving
                moving = 1 - moving
            else:
                h = h_moving

            max_area = max(max_area, (edges[1] - edges[0]) * h)

        return max_area

    def maxArea_simple(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
