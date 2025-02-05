class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) == 0:
            return True
        elif len(diffs) == 2:
            i, j = diffs
            return s1[i] == s2[j] and s1[j] == s2[i]
        else:
            return False
