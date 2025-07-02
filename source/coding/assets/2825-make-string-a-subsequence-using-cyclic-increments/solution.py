class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n2 = len(str2)
        j = 0
        for c1 in str1:
            if (ord(str2[j]) - ord(c1)) % 26 <= 1:
                j += 1
                if j == n2:
                    return True

        return False
