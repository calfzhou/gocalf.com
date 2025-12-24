class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                temperatures[j] = i - j
            stack.append(i)

        for i in stack:
            temperatures[i] = 0

        return temperatures
