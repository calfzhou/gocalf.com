class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pairs: set[str] = set()
        for i in range(len(s) - 1):
            t = s[i:i+2]
            pairs.add(t)
            if t[::-1] in pairs:
                return True

        return False
