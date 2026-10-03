class ForgetfulList:
    def __init__(self, limit: int, default: int = None, cnt: int = 0):
        """Inits a forgetful list which can remember at most `limit` recent values.
        The first `cnt` values will be set to `default`.
        """
        self._limit = limit
        self._buffer = [default] * limit
        self._pos = cnt % self._limit

    def __getitem__(self, idx: int) -> int:
        return self._buffer[idx % self._limit]

    def __setitem__(self, idx: int, val: int):
        self._buffer[idx % self._limit] = val

    def append(self, val: int):
        self._buffer[self._pos] = val
        self._pos = (self._pos + 1) % self._limit


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums = [val for val in nums if val <= target]
        if not nums:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        cw = ForgetfulList(max_val, 0, min_val)
        cw[0] = 1
        for amt in range(min_val, target + 1):
            cw.append(sum(cw[amt - val] for val in nums if amt >= val))

        return cw[target]
