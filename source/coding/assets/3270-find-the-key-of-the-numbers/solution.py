class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        key = 0
        base = 1
        for _ in range(4):
            d = 9
            for j in range(3):
                nums[j], r = divmod(nums[j], 10)
                if r < d: d = r
            key += d * base
            base *= 10

        return key
