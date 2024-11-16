class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        chars = set(s)
        max_len = 0

        for c in chars:
            i = 0
            j = 0
            used = 0
            while j < n:
                if s[j] == c:
                    j += 1
                elif used < k:
                    used += 1
                    j += 1
                else:
                    if s[i] != c:
                        used -= 1
                    i += 1

                max_len = max(max_len, j - i)

        return max_len
