class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - 97] += 1

        for c in t:
            counts[ord(c) - 97] -= 1

        return not any(counts)
