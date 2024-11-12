class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        zero = ord('0')
        digits = [0, 0] # Number of '0's and '1's.
        i, j = 0, -1
        while True:
            if digits[0] <= k or digits[1] <= k:
                j += 1
                if j >= n:
                    break
                digits[ord(s[j]) - zero] += 1
            else:
                count += j - i
                digits[ord(s[i]) - zero] -= 1
                i += 1

        m = j - i
        count += (m * (m + 1)) >> 1
        return count
