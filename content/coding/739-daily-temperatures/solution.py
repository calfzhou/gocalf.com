class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()

            if stack: answer[i] = stack[-1] - i
            stack.append(i) # t is greater than temperatures[stack[-1]].

        return answer
