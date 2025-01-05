from collections import Counter


class Solution:
    def subsequencesWithMiddleMode(self, nums: list[int]) -> int:
        n = len(nums)
        right_counts = {num: cnt for num, cnt in Counter(nums).items() if cnt > 1}
        left_counts = {num: 0 for num in right_counts}

        MOD = 1_000_000_007
        nC2 = lambda n: n * (n - 1) >> 1

        sum_l_r = 0 # \sum_b{l_b ⋅ r_b}
        sum_l_r2 = 0 # \sum_b{l_b ⋅ r_b^2}
        sum_l2_r = 0 # \sum_b{l_b^2 ⋅ r_b}
        sum_l2_l = 0 # \sum_b{l_b^2 - l_b}
        sum_r2_r = sum(r * r - r for r in right_counts.values()) # \sum_b{r_b^2 - r_b}

        total = 0
        r = n
        for l in range(n - 2):
            r -= 1
            a = nums[l]
            if a not in right_counts: continue

            la = left_counts[a]
            ra = right_counts[a]
            sum_l_r -= la * ra
            sum_l_r2 -= la * ra * ra
            sum_l2_r -= la * la * ra
            sum_l2_l -= la * la - la
            sum_r2_r -= ra * ra - ra

            right_counts[a] -= 1
            ra -= 1

            if l > 1:
                cnt = nC2(l) * nC2(r)
                cnt -= nC2(l - la) * nC2(r - ra)
                cnt -= sum_l_r * (r * la + l * ra - 2 * la * ra) - sum_l_r2 * la - sum_l2_r * ra
                cnt -= (sum_l2_l * (r - ra) * ra + sum_r2_r * (l - la) * la) >> 1
                total = (total + cnt) % MOD

            left_counts[a] += 1
            la += 1

            sum_l_r += la * ra
            sum_l_r2 += la * ra * ra
            sum_l2_r += la * la * ra
            sum_l2_l += la * la - la
            sum_r2_r += ra * ra - ra

        return total
