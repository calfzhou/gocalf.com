class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(s[i] != s[i-1] and 1 or 0 for i in range(1, len(s)))
