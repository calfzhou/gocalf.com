class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = list(range(1, n + 2)) # [1, 2, 3, ..., n+1]
        i = 0
        while i < n:
            if pattern[i] == 'D':
                j = i
                while j < n and pattern[j] == 'D':
                    j += 1
                result[i:j+1] = range(j+1, i, -1)
                i = j
            i += 1

        return ''.join(map(str, result))
