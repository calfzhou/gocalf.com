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
                al = left_counts[a]
                ar = right_counts[a]
                cnt = nC2(l) * nC2(r)
                cnt -= nC2(l - al) * nC2(r - ar)
                for b in right_counts:
                    if b == a: continue
                    bl = left_counts[b]
                    br = right_counts[b]
                    if bl + br < 2: continue
                    if al > 0:
                        cnt -= al * bl * br * (r - ar - br)
                        cnt -= al * (l - al) * nC2(br)
                    if ar > 0:
                        cnt -= ar * bl * br * (l - al - bl)
                        cnt -= ar * (r - ar) * nC2(bl)
                total = (total + cnt) % MOD

            left_counts[a] += 1

        return total
