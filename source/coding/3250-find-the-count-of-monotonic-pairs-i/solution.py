class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        a_max = nums[-1]
        prev_val = nums[0]
        prev_a_min = 0
        prev_cnts = [1] * (a_max + 1)
        cnts = [1] * (a_max + 1)

        for i in range(1, len(nums)):
            val = nums[i]
            a_min = max(prev_a_min, prev_a_min + val - prev_val)
            if a_min > val or a_min > a_max:
                return 0

            # p = min(a_min, prev_val, prev_val - val + a_min)
            p = min(a_min, prev_val - val + a_min)
            cnt = sum(prev_cnts[prev_a_min:p+1]) % MOD
            cnts[a_min] = cnt
            for a in range(a_min + 1, min(val, a_max) + 1):
                # if min(a, prev_val - val + a) > p:
                p += 1
                cnt += prev_cnts[p]
                cnts[a] = cnt

            prev_val = val
            prev_a_min = a_min
            prev_cnts, cnts = cnts, prev_cnts

        return sum(prev_cnts[prev_a_min:]) % MOD
