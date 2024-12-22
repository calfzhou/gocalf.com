from bisect import bisect_left, insort


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        answer = [-1] * len(queries)
        queries2 = []
        for i, (a, b) in enumerate(queries):
            if a == b:
                answer[i] = b
                continue
            elif a > b:
                a, b = b, a

            if heights[a] < heights[b]:
                answer[i] = b
            else:
                queries2.append((heights[a], b, i))
        queries2.sort(reverse=True)

        n = len(heights)
        h_indices = sorted(range(n), key=lambda j: heights[j], reverse=True)
        candidates = []

        j = 0
        for height, b, i in queries2:
            while j < n and heights[h_indices[j]] > height:
                insort(candidates, h_indices[j])
                j += 1

            idx = bisect_left(candidates, b)
            if idx < len(candidates):
                answer[i] = candidates[idx]

        return answer
