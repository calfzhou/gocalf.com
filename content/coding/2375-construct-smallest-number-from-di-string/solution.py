class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        m = n + 1
        used = [False] * (m + 1)
        result = [0] * m

        def backtrack(i: int) -> bool:
            if i == m:
                return True

            lo, hi = 1, m
            if i > 0:
                if pattern[i - 1] == 'I':
                    lo = result[i - 1] + 1
                else:
                    hi = result[i - 1] - 1

            for d in range(lo, hi + 1):
                if not used[d]:
                    used[d] = True
                    result[i] = d
                    if backtrack(i + 1):
                        return True
                    used[d] = False

            return False

        backtrack(0)
        return ''.join(map(str, result))
