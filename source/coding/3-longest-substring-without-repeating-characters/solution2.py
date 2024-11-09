class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
           return n

        i, j = 0, 1
        max_len = j - i
        chars = {s[i]: i}
        while j < n:
            # Current substring is s[i:j].
            # Try extend it to s[i:j+1].
            # Check if there is a `k`, i <= k < j, s[k] == s[j].
            # Also update chars, remove s[i:k+1], add s[j].
            k = chars.get(s[j], -1)
            while i <= k:
                chars.pop(s[i])
                i += 1

            chars[s[j]] = j

            j += 1
            max_len = max(max_len, j - i)

        return max_len
