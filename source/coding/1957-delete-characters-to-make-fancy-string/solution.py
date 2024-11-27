class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        parts = [s[:2]]
        for i in range(2, n):
            if s[i] != s[i-1] or s[i] != s[i-2]:
                parts.append(s[i])
        return ''.join(parts)
