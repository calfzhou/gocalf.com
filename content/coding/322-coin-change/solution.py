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
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins = [val for val in coins if val <= amount] # To avoid coin assassins (huge-value coins).
        if not coins:
            return -1

        min_val = max_val = coins[0]
        for val in coins:
            if val > max_val:
                max_val = val
            elif val < min_val:
                min_val = val

        mc = ForgetfulList(max_val, amount + 1, min_val)
        mc[0] = 0
        for amt in range(min_val, amount + 1):
            mc.append(min(mc[amt - val] + 1 for val in coins if amt >= val))

        return -1 if mc[amount] > amount else mc[amount]
