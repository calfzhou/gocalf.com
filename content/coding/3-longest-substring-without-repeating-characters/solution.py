class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
           return n

        i, j = 0, 1
        max_len = j - i
        while j < n:
            # Current substring is s[i:j].
            # Try extend it to s[i:j+1].
            # Check if there is a `k`, i <= k < j, s[k] == s[j].
            for k in range(i, j):
                if s[k] == s[j]:
                    i = k + 1
                    break

            j += 1
            max_len = max(max_len, j - i)

        return max_len
