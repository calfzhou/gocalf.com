class Solution:
    def numDecodings(self, s: str) -> int:
        p = pp = 1 if '1' <= s[0] <= '9' else 0
        for i in range(1, len(s)):
            if pp == 0 and p == 0:
                break

            w = 0
            if '1' <= s[i] <= '9':
                w += p
            if '10' <= s[i-1:i+1] <= '26':
                w += pp
            pp, p = p, w

        return p
