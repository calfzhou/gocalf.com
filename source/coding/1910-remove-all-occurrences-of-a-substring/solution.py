class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack: list[str] = []
        m = len(part)
        for c in s:
            stack.append(c)
            if len(stack) < m:
                continue

            for i in range(-1, -m - 1, -1):
                if stack[i] != part[i]:
                    break
            else:
                for _ in range(m):
                    stack.pop()

        return ''.join(stack)
