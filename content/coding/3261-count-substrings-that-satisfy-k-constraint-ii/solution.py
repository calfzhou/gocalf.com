from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        lens: list[int] = list(range(n, 0, -1)) # lens[i]: the max length of k-substrings starting at i.
        totals: list[int] = [0] * (n + 1) # totals[j]: the number of k-substrings ending before j.
        zero = ord('0')
        digits = [0, 0] # Number of '0's and '1's.
        i, j = 0, -1
        while True:
            if digits[0] <= k or digits[1] <= k:
                j += 1
                if j > 0:
                    totals[j] = totals[j - 1] + j - i
                if j >= n:
                    break
                digits[ord(s[j]) - zero] += 1
            else:
                lens[i] = j - i
                digits[ord(s[i]) - zero] -= 1
                i += 1

        result = [0] * len(queries)
        for idx, (l, r) in enumerate(queries):
            left = min(lens[l], r - l + 1)
            cnt1 = left * (left + 1) >> 1
            cnt2 = totals[r + 1] - totals[l + left]
            result[idx] = cnt1 + cnt2

        return result
