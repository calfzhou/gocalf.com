from collections import Counter


class Solution:
    def subsequencesWithMiddleMode(self, nums: list[int]) -> int:
        n = len(nums)
        right_counts = {num: cnt for num, cnt in Counter(nums).items() if cnt > 1}
        left_counts = {num: 0 for num in right_counts}

        MOD = 1_000_000_007
        nC2 = lambda n: n * (n - 1) >> 1
        total = 0
        r = n
        for l in range(n - 2):
            r -= 1
            a = nums[l]
            if a not in right_counts: continue
            right_counts[a] -= 1

            if l > 1:
                la = left_counts[a]
                ra = right_counts[a]
                cnt = nC2(l) * nC2(r)
                cnt -= nC2(l - la) * nC2(r - ra)
                for b in right_counts:
                    if b == a: continue
                    lb = left_counts[b]
                    rb = right_counts[b]
                    if lb + rb < 2: continue
                    if la > 0:
                        cnt -= la * lb * rb * (r - ra - rb)
                        cnt -= la * (l - la) * nC2(rb)
                    if ra > 0:
                        cnt -= ra * lb * rb * (l - la - lb)
                        cnt -= ra * (r - ra) * nC2(lb)
                total = (total + cnt) % MOD

            left_counts[a] += 1

        return total
