from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_left_area = self._max_left_area(height)
        height.reverse()
        max_right_area = self._max_left_area(height)
        return max(max_left_area, max_right_area)

    def _max_left_area(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        # $\forall j\in fences,\forall 1\le p< j,h_p< h_j$
        fences = [0]
        max_height = heights[0]
        for i in range(1, n):
            h_i = heights[i]
            if max_height < h_i:
                fences.append(i)
                max_height = h_i
                continue

            j = self._find_min_ge(fences, heights, h_i)
            max_area = max(max_area, (i - j) * h_i)

        return max_area

    def _find_min_ge_slow(self, fences: List[int], heights: List[int], h: int) -> int:
        for j in fences:
            if heights[j] >= h:
                return j

    def _find_min_ge(self, fences: List[int], heights: List[int], h: int) -> int:
        """Finds the minimal j, where j in fences, and heights[j-1] < h <= heights[j].

        Constraints:

        - heights[fences[-1]] >= h
        """
        l, r = 0, len(fences) - 1
        while l <= r:
            m = (l + r) >> 1
            if (m_h := heights[fences[m]]) == h:
                return fences[m]
            elif m_h < h:
                l = m + 1
            else:
                r = m - 1

        return fences[l] if heights[fences[l]] > h else fences[l + 1]
