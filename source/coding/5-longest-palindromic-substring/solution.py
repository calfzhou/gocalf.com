class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = [1, 0] # [length, begin position]

        def find_palindromic(mid, odd):
            l, r = mid - (odd and 1 or 0), mid + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1

            m = r - l - 1
            if m > longest[0]:
                longest[0] = m
                longest[1] = l + 1

        for i in range(n):
            # Check longest odd palindromic substring where s[i] is middle.
            find_palindromic(i, True)
            # Check longest even palindromic substring where s[i] and s[i+1] together are middle.
            find_palindromic(i, False)

        m, l = longest
        return s[l:l+m]
