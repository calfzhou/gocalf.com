from bisect import bisect_left


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        answer = [-1] * len(queries)
        # queries2[b]: a list of (heights[a], i) generated from `queries[i] = (a, b)`.
        queries2: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for i, (a, b) in enumerate(queries):
            if a == b:
                answer[i] = b
                continue
            elif a > b:
                a, b = b, a

            if heights[a] < heights[b]:
                answer[i] = b
            else:
                queries2[b].append((heights[a], i))

        stack = []
        for i in range(n - 1, -1, -1):
            height = heights[i]
            while stack and heights[stack[-1]] <= height:
                stack.pop()

            for h, j in queries2[i]:
                idx = bisect_left(stack, -h, key=lambda k: -heights[k]) - 1
                if idx >= 0:
                    answer[j] = stack[idx]

            stack.append(i)

        return answer
