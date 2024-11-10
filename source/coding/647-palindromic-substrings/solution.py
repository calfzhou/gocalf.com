class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count_palindromic(mid, odd):
            l, r = mid - (odd and 1 or 0), mid + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1

            # For a 2k-1 length odd palindromic, counting as k.
            # For a 2k length even palindromic, counting as k.
            # Here the palindromic length is r - l - 1.
            # If r - l - 1 is odd, k = (r - l) / 2.
            # If r - l - 1 is even, k = (r - l - 1) / 2 = (r - l) // 2.
            return (r - l) >> 1

        count = 0
        for i in range(n):
            # Check longest odd palindromic substring where s[i] is middle.
            count += count_palindromic(i, True)
            # Check longest even palindromic substring where s[i] and s[i+1] together are middle.
            count += count_palindromic(i, False)

        return count
